$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Web
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$imgDir = Join-Path $root 'images'
New-Item -ItemType Directory -Force $imgDir | Out-Null
$all = Get-Content "$env:TEMP\swansura_products.json" -Raw -Encoding utf8 | ConvertFrom-Json

function BrandOf($p) {
  if ($p.title -match '^Deyga') { return 'Deyga' }
  if ($p.title -match 'Vilvah') { return 'Vilvah' }
  if ($p.vendor -like 'anatom*') { return 'anatome' }
  return $p.vendor
}
$plan = [ordered]@{ 'Deyga'=8; 'Vilvah'=8; 'Highborn London'=4; 'anatome'=4; 'Tiziana Terenzi'=5; 'Al Haramain'=6; 'Hemel'=4; 'Signature D''orient'=3; 'Fumeri'=3; 'Gucci'=3 }
$fragBrands = 'Tiziana Terenzi','Al Haramain','Hemel','Signature D''orient','Fumeri','Gucci'

function CleanText($html) {
  if (-not $html) { return '' }
  $t = $html -replace '(?i)<br\s*/?>', "`n" -replace '(?i)</(p|li|h\d|div)>', "`n" -replace '(?i)<li[^>]*>', '- '
  $t = [regex]::Replace($t, '<[^>]+>', '')
  $t = [System.Web.HttpUtility]::HtmlDecode($t)
  $t = [regex]::Replace($t, '[ \t]+', ' ')
  $lines = $t -split "`n" | ForEach-Object { $_.Trim() } | Where-Object { $_ -and $_ -notmatch '(?i)^(barcode|ean|upc)\b' -and $_ -notmatch '^\d{8,}$' }
  return ($lines -join "`n")
}
function CategoryOf($p, $brand) {
  $t = $p.title
  if ($fragBrands -contains $brand -or $t -match '(?i)parfum|\bEDP\b|\bEDT\b|perfume|eau de|fragrance') { return 'fragrance' }
  if ($t -match '(?i)shampoo|conditioner|hair') { return 'haircare' }
  if ($t -match '(?i)body|soap|bath|butter|pillow|sleep|hand cream|foot') { return 'bath-body' }
  return 'skincare'
}
function Tags($p, $cat) {
  $t = ($p.title + ' ' + $p.body_html)
  $tags = @()
  if ($p.title -match '(?i)\b(kit|combo|set|duo|trio|bundle|gift)\b') { $tags += 'gift' }
  if ($cat -eq 'fragrance') {
    if ($t -match '(?i)oud') { $tags += 'oud' }
    if ($t -match '(?i)floral|rose|jasmine') { $tags += 'floral' }
    if ($t -match '(?i)wood|cedar|sandal|vetiver|patchouli') { $tags += 'woody' }
    if ($t -match '(?i)amber|oriental|vanilla') { $tags += 'amber' }
    if ($t -match '(?i)fresh|citrus|aquatic|bergamot') { $tags += 'fresh' }
    if ($p.title -match '(?i)\bmen\b|homme|for men') { $tags += 'men' } elseif ($p.title -match '(?i)women|femme') { $tags += 'women' } else { $tags += 'unisex' }
  } else {
    if ($t -match '(?i)acne|pimple|charcoal|tea tree|oil control') { $tags += 'acne' }
    if ($t -match '(?i)pigment|dark spot|bright|vitamin c|glow|\btan\b') { $tags += 'glow' }
    if ($t -match '(?i)dry skin|hydrat|moistur|hyaluronic|aloe') { $tags += 'hydration' }
    if ($t -match '(?i)hair ?fall|hair growth|onion') { $tags += 'hairfall' }
    if ($t -match '(?i)dandruff') { $tags += 'dandruff' }
    if ($p.title -match '(?i)\blip') { $tags += 'lips' }
    if ($t -match '(?i)sunscreen|spf') { $tags += 'sun' }
    if ($t -match '(?i)sleep|relax|calm') { $tags += 'calm' }
  }
  return $tags
}
function ShortTitle($t) {
  $s = ($t -split ' [–|-] ')[0]
  $s = $s -replace '\s+\|.*$', ''
  return $s.Trim()
}

$ivory = [System.Drawing.Color]::FromArgb(242, 237, 228)
$cm = New-Object System.Drawing.Imaging.ColorMatrix
$cm.Matrix00 = [single](0.949 * 1.04); $cm.Matrix11 = [single](0.929 * 1.04); $cm.Matrix22 = [single](0.894 * 1.04)
$cm.Matrix40 = [single]-0.02; $cm.Matrix41 = [single]-0.02; $cm.Matrix42 = [single]-0.02
$attr = New-Object System.Drawing.Imaging.ImageAttributes
$attr.SetColorMatrix($cm)
$jpg = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$ep = New-Object System.Drawing.Imaging.EncoderParameters 1
$ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), 80L
$wc = New-Object System.Net.WebClient

function ProcessImage($url, $outName) {
  $out = Join-Path $imgDir $outName
  if (Test-Path $out) { return $true }
  try {
    $src = $url + $(if ($url -match '\?') { '&' } else { '?' }) + 'width=1000'
    $bytes = $wc.DownloadData($src)
    $ms = New-Object System.IO.MemoryStream(, $bytes)
    $img = [System.Drawing.Image]::FromStream($ms)
    $canvasW = 800; $canvasH = 1000
    $bmp = New-Object System.Drawing.Bitmap $canvasW, $canvasH
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = 'HighQualityBicubic'; $g.SmoothingMode = 'HighQuality'; $g.PixelOffsetMode = 'HighQuality'
    $g.Clear($ivory)
    $pad = 0.86
    $scale = [Math]::Min(($canvasW * $pad) / $img.Width, ($canvasH * $pad) / $img.Height)
    $drawW = [int]($img.Width * $scale); $drawH = [int]($img.Height * $scale)
    $offX = [int](($canvasW - $drawW) / 2); $offY = [int](($canvasH - $drawH) / 2)
    $rect = New-Object System.Drawing.Rectangle $offX, $offY, $drawW, $drawH
    $g.DrawImage($img, $rect, 0, 0, $img.Width, $img.Height, [System.Drawing.GraphicsUnit]::Pixel, $attr)
    $bmp.Save($out, $jpg, $ep)
    $g.Dispose(); $bmp.Dispose(); $img.Dispose(); $ms.Dispose()
    return $true
  } catch { Write-Warning "img fail $url : $($_.Exception.Message)"; return $false }
}

$out = @()
foreach ($brand in $plan.Keys) {
  $n = $plan[$brand]
  $cands = @($all | Where-Object { (BrandOf $_) -eq $brand -and $_.images.Count -gt 0 -and [double]$_.variants[0].price -gt 0 })
  $avail = @($cands | Where-Object { @($_.variants | Where-Object { $_.available }).Count -gt 0 })
  if ($avail.Count -ge $n) { $cands = $avail }
  $pref = @{ 'Deyga' = 'Beetroot Lip Balm Classic|Charcoal Face Wash|Sunscreen 50|Rose Glow Serum|Body Butter|Rice Water Shampoo|Shea Saffron Bath Bar|Hyaluronic'; 'Vilvah' = 'Milk Drops Hydrating|Goat Milk Shampoo|Tinted Lip Balm Kit|Ultra Moisturising|Hair Growth Oil|Better Ageing|Milk Powder Face Wash|Aloe Vera Gel'; 'anatome' = 'Pillow Spray|Sleep Oil|Bath Salts|Focus Eau' }
  $first = @()
  if ($pref.ContainsKey($brand)) { foreach ($k in ($pref[$brand] -split '\|')) { $m = $cands | Where-Object { $_.title -match [regex]::Escape($k) } | Select-Object -First 1; if ($m) { $first += $m } } }
  $rest = @($cands | Where-Object { $first.id -notcontains $_.id } | Sort-Object { -1 * $_.images.Count })
  $picked = @(($first + $rest) | Select-Object -First $n)
  foreach ($p in $picked) {
    $cat = CategoryOf $p $brand
    $imgs = @()
    $i = 0
    foreach ($im in ($p.images | Select-Object -First 3)) {
      $i++
      $h = $p.handle.Substring(0, [Math]::Min(50, $p.handle.Length))
      $name = "$h-$i.jpg"
      if (ProcessImage $im.src $name) { $imgs += "images/$name" }
    }
    if ($imgs.Count -eq 0) { continue }
    $v = $p.variants[0]
    $out += [ordered]@{
      id = "$($p.id)"; handle = $p.handle; title = (ShortTitle $p.title); fullTitle = $p.title; brand = $brand; cat = $cat
      price = [double]$v.price; compare = $(if ($v.compare_at_price -and [double]$v.compare_at_price -gt [double]$v.price) { [double]$v.compare_at_price } else { $null })
      size = $(if ($v.title -and $v.title -ne 'Default Title') { $v.title } else { '' })
      available = (@($p.variants | Where-Object { $_.available }).Count -gt 0)
      tags = @(Tags $p $cat); desc = (CleanText $p.body_html); images = $imgs
    }
  }
}
$json = ConvertTo-Json -InputObject $out -Depth 6
[System.IO.File]::WriteAllText((Join-Path $root 'products.json'), $json, (New-Object System.Text.UTF8Encoding $false))
"products=$($out.Count) images=$((Get-ChildItem $imgDir).Count) sizeMB=$([Math]::Round(((Get-ChildItem $imgDir | Measure-Object Length -Sum).Sum/1MB),1))"
$out | ForEach-Object { "$($_.brand) | $($_.cat) | $($_.title) | $($_.price) | $($_.tags -join ',') | imgs $($_.images.Count) | desc $($_.desc.Length)" }

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Web
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$imgDir = Join-Path $root 'img'
New-Item -ItemType Directory -Force $imgDir | Out-Null

# Fresh catalogue
$all = @()
for ($p = 1; $p -le 6; $p++) {
  $r = Invoke-RestMethod "https://www.swansura.com/products.json?limit=250&page=$p"
  if ($r.products.Count -eq 0) { break }
  $all += $r.products
}
$all = @($all | Where-Object { $_.title -notmatch '(?i)example product' -and $_.handle -notmatch 'example' })

$vendorMap = @{
  'antonio'='Antonio Banderas'; 'Tomford'='Tom Ford'; 'HugoBoss'='Hugo Boss'; 'dior'='Dior'; 'phillip plein'='Philipp Plein';
  'joop homme'='Joop!'; 'Abercrombie& fitch'='Abercrombie & Fitch'; 'anna sui'='Anna Sui'; 'ariana grande'='Ariana Grande';
  'john varvatos'='John Varvatos'; 'Jean Paul'='Jean Paul Gaultier'; 'Calvin klein'='Calvin Klein'; 'vilvah STORE'='Vilvah'; 'YSL'='Yves Saint Laurent'; 'Chloe'='Chloé'
}
function BrandOf($p) {
  $t = $p.title
  if ($t -match '(?i)\bdeyga') { return 'Deyga' }
  if ($t -match '(?i)\bvilvah') { return 'Vilvah' }
  if ($t -match '(?i)^herm') { return 'Hermès' }
  if ($t -match '(?i)acqua di parma') { return 'Acqua di Parma' }
  if ($t -match '(?i)anniversary extrait') { return 'Tiziana Terenzi' }
  if ($t -match '(?i)^korloff') { return 'Korloff' }
  if ($p.vendor -like 'anatom*') { return 'anatomē' }
  if ($p.vendor -in 'Generic', 'Swansura - The Body Studio') {
    $b = $p.body_html
    if ($b -match '(?i)deyga') { return 'Deyga' }
    if ($b -match '(?i)vilvah') { return 'Vilvah' }
    return 'Swansura Selection'
  }
  if ($vendorMap.ContainsKey($p.vendor)) { return $vendorMap[$p.vendor] }
  return $p.vendor
}
$skinBrands = 'Deyga', 'Vilvah', 'Highborn London', 'Swansura Selection'
function CategoryOf($p, $brand) {
  $t = $p.title
  if ($t -match '(?i)parfum|\bEDP\b|\bEDT\b|perfume|eau de|fragrance|cologne|attar|\bmist\b' -and $t -notmatch '(?i)fragrance[- ]free') { return 'fragrance' }
  if ($t -match '(?i)shampoo|conditioner|hair|scalp|frizz|dandruff') { return 'haircare' }
  if ($t -match '(?i)body|soap|bath|butter|pillow|sleep|hand cream|foot|deo|roll it|scrub') { return 'bath-body' }
  if ($skinBrands -contains $brand -or $brand -eq 'anatomē') { return 'skincare' }
  return 'fragrance'
}
function Tags($p, $cat) {
  $t = ($p.title + ' ' + $p.body_html)
  $tags = @()
  if ($p.title -match '(?i)\b(kit|combo|set|duo|trio|bundle|gift|minis?|miniature|discovery)\b') { $tags += 'gift' }
  if ($cat -eq 'fragrance') {
    if ($t -match '(?i)oud') { $tags += 'oud' }
    if ($t -match '(?i)floral|rose|jasmine') { $tags += 'floral' }
    if ($t -match '(?i)wood|cedar|sandal|vetiver|patchouli') { $tags += 'woody' }
    if ($t -match '(?i)amber|oriental|vanilla') { $tags += 'amber' }
    if ($t -match '(?i)fresh|citrus|aquatic|bergamot') { $tags += 'fresh' }
    if ($p.title -match '(?i)\bmen\b|men.s|homme|for him|pour lui') { $tags += 'men' } elseif ($p.title -match '(?i)women|femme|for her|pour elle') { $tags += 'women' } else { $tags += 'unisex' }
  } else {
    if ($t -match '(?i)acne|pimple|charcoal|tea tree|oil control|neem') { $tags += 'acne' }
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
function CleanText($html) {
  if (-not $html) { return '' }
  $t = $html -replace '(?i)<br\s*/?>', "`n" -replace '(?i)</(p|li|h\d|div)>', "`n" -replace '(?i)<li[^>]*>', '- '
  $t = [regex]::Replace($t, '<[^>]+>', '')
  $t = [System.Web.HttpUtility]::HtmlDecode($t)
  $t = [regex]::Replace($t, '[ \t]+', ' ')
  $lines = $t -split "`n" | ForEach-Object { $_.Trim() } | Where-Object { $_ -and $_ -notmatch '(?i)^(barcode|ean|upc)\b' -and $_ -notmatch '^\d{8,}$' }
  $s = ($lines -join "`n")
  if ($s.Length -gt 1800) { $s = $s.Substring(0, 1800) }
  return $s
}

$ivory = [System.Drawing.Color]::FromArgb(242, 237, 228)
$cm = New-Object System.Drawing.Imaging.ColorMatrix
$cm.Matrix00 = [single](0.949 * 1.04); $cm.Matrix11 = [single](0.929 * 1.04); $cm.Matrix22 = [single](0.894 * 1.04)
$cm.Matrix40 = [single]-0.02; $cm.Matrix41 = [single]-0.02; $cm.Matrix42 = [single]-0.02
$attr = New-Object System.Drawing.Imaging.ImageAttributes
$attr.SetColorMatrix($cm)
$jpg = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$ep = New-Object System.Drawing.Imaging.EncoderParameters 1
$ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), 76L
$wc = New-Object System.Net.WebClient

function BuildStrip($urls, $outPath) {
  $frameW = 640; $frameH = 800
  $imgs = @()
  foreach ($u in $urls) {
    try {
      $src = $u + $(if ($u -match '\?') { '&' } else { '?' }) + 'width=900'
      $bytes = $wc.DownloadData($src)
      $ms = New-Object System.IO.MemoryStream(, $bytes)
      $imgs += [System.Drawing.Image]::FromStream($ms)
    } catch { Write-Warning "img fail $u" }
  }
  if ($imgs.Count -eq 0) { return 0 }
  $bmp = New-Object System.Drawing.Bitmap $frameW, ($frameH * $imgs.Count)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.InterpolationMode = 'HighQualityBicubic'; $g.SmoothingMode = 'HighQuality'; $g.PixelOffsetMode = 'HighQuality'
  $g.Clear($ivory)
  for ($i = 0; $i -lt $imgs.Count; $i++) {
    $img = $imgs[$i]
    $scale = [Math]::Min(($frameW * 0.86) / $img.Width, ($frameH * 0.86) / $img.Height)
    $drawW = [int]($img.Width * $scale); $drawH = [int]($img.Height * $scale)
    $offX = [int](($frameW - $drawW) / 2); $offY = [int](($frameH - $drawH) / 2) + $frameH * $i
    $rect = New-Object System.Drawing.Rectangle $offX, $offY, $drawW, $drawH
    $g.DrawImage($img, $rect, 0, 0, $img.Width, $img.Height, [System.Drawing.GraphicsUnit]::Pixel, $attr)
    $img.Dispose()
  }
  $bmp.Save($outPath, $jpg, $ep)
  $g.Dispose(); $bmp.Dispose()
  return $imgs.Count
}

$out = @(); $n = 0
foreach ($p in $all) {
  $n++
  if ($p.images.Count -eq 0) { continue }
  $brand = BrandOf $p
  $cat = CategoryOf $p $brand
  $file = "img/$($p.id).jpg"
  $path = Join-Path $root $file
  $metaPath = "$path.frames"
  if ((Test-Path $path) -and (Test-Path $metaPath)) { $frames = [int](Get-Content $metaPath) }
  else {
    $frames = BuildStrip @($p.images | Select-Object -First 2 | ForEach-Object { $_.src }) $path
    Set-Content $metaPath $frames
  }
  if ($frames -eq 0) { continue }
  $v = $p.variants[0]
  $out += [ordered]@{
    id = "$($p.id)"; title = $p.title; brand = $brand; cat = $cat
    price = [double]$v.price; compare = $(if ($v.compare_at_price -and [double]$v.compare_at_price -gt [double]$v.price) { [double]$v.compare_at_price } else { $null })
    available = (@($p.variants | Where-Object { $_.available }).Count -gt 0)
    tags = @(Tags $p $cat); desc = (CleanText $p.body_html); img = $file; frames = $frames
  }
  if ($n % 50 -eq 0) { Write-Output "processed $n / $($all.Count)" }
}
$json = ConvertTo-Json -InputObject $out -Depth 6 -Compress
[System.IO.File]::WriteAllText((Join-Path $root 'products.json'), $json, (New-Object System.Text.UTF8Encoding $false))
"DONE products=$($out.Count) of $($all.Count) strips=$((Get-ChildItem $imgDir -Filter *.jpg).Count) sizeMB=$([Math]::Round(((Get-ChildItem $imgDir -Filter *.jpg | Measure-Object Length -Sum).Sum/1MB),1)) jsonKB=$([Math]::Round($json.Length/1KB))"
$out | Group-Object brand | Sort-Object Count -Descending | ForEach-Object { "$($_.Name)=$($_.Count)" }
$out | Group-Object cat | ForEach-Object { "cat $($_.Name)=$($_.Count)" }

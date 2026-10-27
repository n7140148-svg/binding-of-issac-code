param([string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path)

$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath($Root)
$artifactDirectory = Join-Path $Root 'artifacts'
New-Item -ItemType Directory -Path $artifactDirectory -Force | Out-Null
$stage = Join-Path $artifactDirectory ('reference-package-' + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $stage | Out-Null

function Copy-RelativeFile([string]$Relative) {
    $destination = Join-Path $stage $Relative
    New-Item -ItemType Directory -Path ([IO.Path]::GetDirectoryName($destination)) -Force | Out-Null
    Copy-Item -LiteralPath (Join-Path $Root $Relative) -Destination $destination
}

foreach ($file in Get-ChildItem -LiteralPath (Join-Path $Root 'reference') -File -Recurse) {
    $relative = [IO.Path]::GetRelativePath($Root, $file.FullName)
    if ($relative -match '(^|[\\/])(bin|obj)([\\/]|$)') { continue }
    Copy-RelativeFile $relative
}
foreach ($variant in @('focused', 'repaired')) {
    foreach ($file in Get-ChildItem -LiteralPath (Join-Path $Root "evidence/$variant") -Filter '*.txt') {
        Copy-RelativeFile ([IO.Path]::GetRelativePath($Root, $file.FullName))
    }
}
foreach ($relative in @(
    'evidence/manifest.json', 'evidence/pe-constants.json', 'evidence/reference-vectors.json',
    'evidence/seed-string-refs.csv', 'gl_INDEX.md', 'SCOPE.md',
    'reports/FINAL_CODE_2026-10-27.md', 'reports/reference-validation.txt',
    'reports/how_isaac_does_rng.md', 'reports/how_isaac_does_item_pools.md',
    'reports/how_isaac_does_level_generation.md', 'reports/how_isaac_does_combat.md',
    'reports/how_isaac_does_enemy_waves.md',
    'tools/analysis/reference_vectors.mjs', 'tools/analysis/read_pe_constants.mjs',
    'tools/analysis/index_focused.mjs', 'tools/ghidra/DumpFocused.java',
    'tools/ghidra/DumpStringReferences.java', 'tools/ghidra/RepairLoggerFlow.java'
)) { Copy-RelativeFile $relative }

$runtime = Join-Path $stage 'runtime'
& dotnet publish (Join-Path $Root 'reference/IsaacReference.Runner/IsaacReference.Runner.csproj') -c Release --no-restore --no-self-contained -p:UseAppHost=false --nologo -o $runtime
if ($LASTEXITCODE -ne 0) { throw 'Publish failed.' }

$zip = Join-Path $artifactDirectory 'IsaacReference-2026-10-27.zip'
Compress-Archive -Path (Join-Path $stage '*') -DestinationPath $zip -Force
Write-Output "Package: $zip"
Get-FileHash -LiteralPath $zip -Algorithm SHA256 | Format-List

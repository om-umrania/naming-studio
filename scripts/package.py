"""Build a plugin archive from an explicit public-file allowlist."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_DEFLATED
import argparse
import json
import shutil
from validate import ROOT, validate

parser = argparse.ArgumentParser()
parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
args = parser.parse_args()
validate()
name = json.loads((ROOT / 'plugin.json').read_text())['name']
allowed = ['plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json',
           '.claude-plugin/marketplace.json', '.agents/plugins/marketplace.json',
           'README.md', 'LICENSE', 'CONNECTORS.md']
files = [ROOT / p for p in allowed if (ROOT / p).is_file()]
files += [p for p in (ROOT / 'skills').rglob('*') if p.is_file() and '__pycache__' not in p.parts]
with TemporaryDirectory() as temp:
    archive = Path(temp) / (name + '.plugin')
    with ZipFile(archive, 'w', ZIP_DEFLATED) as bundle:
        for file in sorted(files):
            bundle.write(file, file.relative_to(ROOT))
    with ZipFile(archive) as bundle:
        assert bundle.testzip() is None
        members = bundle.namelist()
        assert len([p for p in members if p.endswith('/SKILL.md')]) == 3
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir.resolve() / archive.name
    shutil.copyfile(archive, destination)
    print(f'Built {destination} ({len(files)} files)')

"""Validate the distributable contract without requiring agent runtimes."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    manifests = [json.loads((root / p).read_text()) for p in
                 ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json')]
    canonical = manifests[0]
    for manifest in manifests:
        for key in ('name', 'version', 'description', 'author'):
            assert manifest[key] == canonical[key], f'Manifest drift: {key}'
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', manifest['name']), 'Invalid plugin name'
        assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version']), 'Invalid version'
    assert manifests[1]['skills'] == './skills/'
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    assert len(skills) == 3, 'V1 requires three skill entrypoints'
    for skill in skills:
        text = skill.read_text()
        assert text.startswith('---\n'), f'Missing frontmatter: {skill}'
        front = text.split('---', 2)[1]
        name = re.search(r'^name: (.+)$', front, re.M)
        assert name and name[1] == skill.parent.name, f'Skill name mismatch: {skill}'
        assert re.search(r'^description: .+', front, re.M), f'Missing description: {skill}'
    for doc in (root / 'skills').rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            destination = (doc.parent / target.split('#')[0]).resolve()
            assert destination.is_relative_to(root.resolve()), f'Link escapes package: {doc}: {target}'
            assert destination.is_file(), f'Broken link: {doc}: {target}'
    for path in ('.claude-plugin/marketplace.json', '.agents/plugins/marketplace.json'):
        market = json.loads((root / path).read_text())
        entries = market['plugins']
        assert len(entries) == 1 and entries[0]['name'] == canonical['name'], f'Marketplace drift: {path}'
        source = entries[0]['source']
        local = source if isinstance(source, str) else source['path']
        assert (root / local).resolve() == root.resolve(), f'Wrong marketplace root: {path}'
    print('PASS: aligned manifests, three skill entrypoints, contained links, marketplace sources')

if __name__ == '__main__':
    validate()

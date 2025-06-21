import os
from datetime import datetime

class WhitepaperGenerator:
    def __init__(self, output_dir="docs"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate(self, project_info):
        filename = os.path.join(self.output_dir, "GAIA_Whitepaper.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {project_info['title']}
")
            f.write(f"**Version**: {project_info.get('version', '1.0')}
")
            f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d')}

")
            f.write(f"## Abstract
{project_info.get('abstract', 'TBD')}

")
            f.write(f"## Introduction
{project_info.get('introduction', 'TBD')}

")
            f.write(f"## Architecture
{project_info.get('architecture', 'TBD')}

")
            f.write(f"## Modules
{project_info.get('modules', 'TBD')}

")
            f.write(f"## Roadmap
{project_info.get('roadmap', 'TBD')}

")
            f.write(f"## Licensing
{project_info.get('licensing', 'TBD')}

")
            f.write(f"## Contact
{project_info.get('contact', 'TBD')}

")
        return filename

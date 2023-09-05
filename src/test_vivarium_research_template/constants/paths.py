from pathlib import Path

import test_vivarium_research_template
from test_vivarium_research_template.constants import metadata

BASE_DIR = Path(test_vivarium_research_template.__file__).resolve().parent

ARTIFACT_ROOT = Path(f"/share/costeffectiveness/artifacts/{metadata.PROJECT_NAME}/")
MODEL_SPEC_DIR = BASE_DIR / "model_specifications"
RESULTS_ROOT = Path(f"/share/costeffectiveness/results/{metadata.PROJECT_NAME}/")

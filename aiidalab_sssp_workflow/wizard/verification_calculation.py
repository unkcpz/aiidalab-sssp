from aiidalab_widgets_base import WizardAppWidgetStep

from aiidalab_sssp_workflow.remake.verification import (
    ComputeVerificationWidget as OldComputeVerificationWidget,
)


class ComputeVerificationWidget(OldComputeVerificationWidget, WizardAppWidgetStep):
    """Wizard step wrapping ComputeVerificationWidget"""

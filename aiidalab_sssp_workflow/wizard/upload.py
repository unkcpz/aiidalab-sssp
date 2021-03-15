from typing import Union

import aiida
from aiidalab_widgets_base import WizardAppWidgetStep
import ipywidgets as ipw
import traitlets

from aiidalab_sssp_workflow.remake.pseudo import PseudoUploadWidget


class UploadPseudoFile(ipw.VBox, WizardAppWidgetStep):
    """Wizard step equivalent to aiidalab_sssp_workflow.old.pseudo.PseudoSelectionWidget"""

    pseudo = traitlets.Instance(aiida.orm.UpfData, allow_none=True)
    confirmed_pseudo = traitlets.Instance(aiida.orm.UpfData, allow_none=True)

    def __init__(self, description: Union[str, ipw.Label] = None, **kwargs) -> None:
        self.pseudo_upload_widget = PseudoUploadWidget(title="From computer")

        if description is None:
            description = ipw.Label(
                "Select a pseudopotential from one of the following sources and then "
                'click "Confirm" to go to the next step.'
            )
        self.description = (
            ipw.Label(description) if isinstance(description, str) else description
        )

        self.pseudo_name_text = ipw.Text(
            placeholder="[No pseudo selected]",
            description="Selected:",
            disabled=True,
            layout=ipw.Layout(width="auto", flex="1 1 auto"),
        )

        self.confirm_button = ipw.Button(
            description="Confirm",
            tooltip="Confirm the currently selected pseudopotential and go to the next step.",
            button_style="success",
            icon="check-circle",
            disabled=True,
            layout=ipw.Layout(width="auto"),
        )
        self.confirm_button.on_click(self.confirm)

        # Create directional link from the (read-only) 'pseudo_node' traitlet of the
        # pseudo upload widget to our 'pseudo' traitlet:
        ipw.dlink((self.pseudo_upload_widget, "pseudo_node"), (self, "pseudo"))

        super().__init__(
            children=(
                self.description,
                self.pseudo_upload_widget,
                self.pseudo_name_text,
                self.confirm_button,
            ),
            **kwargs,
        )

    def confirm(self, _=None) -> None:
        """Confirm chosen pseudopotential"""
        self.confirmed_pseudo = self.pseudo

    def reset(self) -> None:
        """Reset widget

        This will "un"-confirm the chosen pseudopotential.
        """
        self.confirmed_pseudo = None

    @traitlets.default("state")
    def _default_state(self) -> WizardAppWidgetStep.State:
        """The default Wizard state."""
        return self.State.READY

    @traitlets.observe("state")
    def _observe_state(self, change: dict) -> None:
        with self.hold_trait_notifications():
            state = change["new"]
            self.confirm_button.disabled = state != self.State.CONFIGURED
            self.manager.disabled = state is self.State.SUCCESS

    @traitlets.observe("pseudo")
    def _observe_pseudo(self, change: dict) -> None:
        """Update pseudo name and state according to new change."""
        pseudo = change["new"]
        self.pseudo_name_text = (
            "" if pseudo is None else f"{self.pseudo.element} ({self.pseudo.filename})"
        )
        with self.hold_trait_notifications():
            self._update_state()

    @traitlets.observe("confirmed_pseudo")
    def _observe_confirmed_pseudo(self, _) -> None:
        """Update state according to new confirmed pseudo."""
        with self.hold_trait_notifications():
            self._update_state()

    def _update_state(self) -> None:
        """Update the Wizard state according to current traitlets."""
        if self.pseudo is None:
            self.state = (
                self.State.READY
                if self.confirmed_pseudo is None
                else self.State.SUCCESS
            )
        else:
            self.state = (
                self.State.CONFIGURED
                if self.confirmed_pseudo is None
                else self.State.SUCCESS
            )

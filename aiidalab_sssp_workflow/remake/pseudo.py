import io

from aiida.orm.nodes.data.upf import UpfData
import ipywidgets as ipw
import traitlets


class PseudoUploadWidget(ipw.VBox):
    """Class that allows to upload pseudopotential from user's computer."""

    pseudo_node = traitlets.Instance(UpfData, allow_none=True)

    def __init__(
        self, title: str = "", description: str = "Upload Pseudopotential"
    ) -> None:
        self.title = title
        self.file_upload = ipw.FileUpload(
            accept=".upf",
            description=description,
            multiple=False,
            layout={"width": "initial"},
        )
        supported_formats = ipw.HTML(
            '<a href="http://www.quantum-espresso.org/pseudopotentials/'
            'unified-pseudopotential-format" target="_blank">Supported pseudo formats</a>'
        )
        self.file_upload.observe(self._on_file_upload, names="value")
        super().__init__(children=(self.file_upload, supported_formats))

    def _on_file_upload(self, change: dict = None) -> None:
        """When file upload button is pressed."""
        for item in change["new"].values():
            try:
                self.pseudo_node = UpfData(file=io.BytesIO(item["content"]))
            except Exception:
                self.pseudo_node = None
            self.file_upload.value.clear()
            break

# -*- coding: utf-8 -*-

import ipywidgets as ipw

template = """
<h3 style="text-align:center">SSSP Workflows</h3>

<table>
  <tr>
    <th>New Apps</th>
    <th>Original Apps</th>
  <tr>
    <td valign="top">
      <ul>
        <li><a href="{appbase}/notebooks/as-wizard.ipynb" target="_blank">Verify a pseudopotential (wizard app)</a></li>
      </ul>
    </td>
    <td valign="top">
      <ul>
        <li><a href="{appbase}/notebooks/sssp-delta-factor.ipynb" target="_blank">delta-factor workflow</a></li>
        <li><a href="{appbase}/notebooks/sssp-verification.ipynb" target="_blank">verification workflow</a></li>
        <li><a href="{appbase}/notebooks/check-verification-results.ipynb" target="_blank"> check verification process</a></li>
        <li><a href="{appbase}/notebooks/bands-chessboard.ipynb" target="_blank">bands chessboard</a></li>
      </ul>
    </td>
  </tr>
</table>
"""


def get_start_widget(appbase, jupbase, notebase):
    html = template.format(appbase=appbase, jupbase=jupbase, notebase=notebase)
    return ipw.HTML(html)


# EOF

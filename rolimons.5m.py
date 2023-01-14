#!/usr/bin/env python3

# <xbar.title>Rolimon's Value Tracker</xbar.title>
# <xbar.version>v1.1</xbar.version>
# <xbar.author.github>JuniorCode</xbar.author.github>
# <xbar.desc>Shows your Rolimon's value.</xbar.desc>
# <xbar.dependencies>python</xbar.dependencies>
# <xbar.abouturl>https://github.com/JuniorCode/rolimons-xbar#readme</xbar.abouturl>
#
# <xbar.var>string(VAR_USER_ID="1"): User ID.</xbar.var>

import os
import json
from urllib.request import urlopen

user_id = os.getenv('VAR_USER_ID')
value = 0

with urlopen('https://www.rolimons.com/itemapi/itemdetails') as r:
    text = r.read()

items = json.loads(text)['items']

with urlopen(f'https://www.rolimons.com/api/playerassets/{user_id}') as r:
    text = r.read()

for item_id, uaids in json.loads(text)['playerAssets'].items():
    value += items[item_id][4] * len(uaids)

print(f'{value:,} | templateImage=PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMTZweCIgaGVpZ2h0PSIxNnB4IiB2aWV3Qm94PSIwIDAgMTYgMTYiIHZlcnNpb249IjEuMSI+CjxnIGlkPSJzdXJmYWNlMSI+CjxwYXRoIHN0eWxlPSIgc3Ryb2tlOm5vbmU7ZmlsbC1ydWxlOm5vbnplcm87ZmlsbDpyZ2IoMCUsMCUsMCUpO2ZpbGwtb3BhY2l0eToxOyIgZD0iTSAyLjAzMTI1IDIuNTU4NTk0IEMgMi4wMzEyNSAzLjk2NDg0NCAyLjAzMTI1IDUuMTE3MTg4IDIuMDM1MTU2IDUuMTE3MTg4IEMgMi4wMzUxNTYgNS4xMTcxODggMi4xMDU0NjkgNS4wODU5MzggMi4xOTE0MDYgNS4wNDY4NzUgQyAyLjI3MzQzOCA1LjAwNzgxMiAyLjM3NSA0Ljk1NzAzMSAyLjQxNzk2OSA0LjkzNzUgQyAyLjQ2MDkzOCA0LjkxNzk2OSAyLjU1ODU5NCA0Ljg3MTA5NCAyLjYzNjcxOSA0LjgzMjAzMSBDIDIuNzY5NTMxIDQuNzY5NTMxIDIuODY3MTg4IDQuNzIyNjU2IDMuMTMyODEyIDQuNTkzNzUgQyAzLjE5OTIxOSA0LjU2MjUgMy4yNTc4MTIgNC41MzkwNjIgMy4yNjE3MTkgNC41MzkwNjIgQyAzLjI2OTUzMSA0LjUzOTA2MiAzLjI3MzQzOCA0LjUzNTE1NiAzLjI3MzQzOCA0LjUyNzM0NCBDIDMuMjczNDM4IDQuNTIzNDM4IDMuMjgxMjUgNC41MTU2MjUgMy4yODkwNjIgNC41MTU2MjUgQyAzLjI5Mjk2OSA0LjUxNTYyNSAzLjM1NTQ2OSA0LjQ4ODI4MSAzLjQyNTc4MSA0LjQ1MzEyNSBDIDMuNDk2MDk0IDQuNDIxODc1IDMuNTU4NTk0IDQuMzk0NTMxIDMuNTcwMzEyIDQuMzk0NTMxIEMgMy41NzgxMjUgNC4zOTQ1MzEgMy42OTE0MDYgNC40NDUzMTIgMy44MjAzMTIgNC41MDc4MTIgQyA0LjA1ODU5NCA0LjYyMTA5NCA0LjQ0NTMxMiA0LjgwNDY4OCA0LjY0NDUzMSA0Ljg5ODQzOCBDIDQuNzAzMTI1IDQuOTI1NzgxIDQuODI4MTI1IDQuOTg4MjgxIDQuOTI1NzgxIDUuMDM1MTU2IEMgNS4wMTk1MzEgNS4wODIwMzEgNS4xMDE1NjIgNS4xMTcxODggNS4xMDE1NjIgNS4xMTcxODggQyA1LjEwMTU2MiA1LjExNzE4OCA1LjE5NTMxMiA1LjE2MDE1NiA1LjMwODU5NCA1LjIxNDg0NCBDIDUuNDIxODc1IDUuMjY5NTMxIDUuNTUwNzgxIDUuMzMyMDMxIDUuNTkzNzUgNS4zNTE1NjIgQyA1LjY2Nzk2OSA1LjM4NjcxOSA1Ljc2OTUzMSA1LjQzNzUgNi4wNjY0MDYgNS41NzgxMjUgQyA2LjE0ODQzOCA1LjYxNzE4OCA2LjIzMDQ2OSA1LjY1NjI1IDYuMjU3ODEyIDUuNjY3OTY5IEwgNi4yOTY4NzUgNS42ODc1IEwgNi4yMDcwMzEgNS43MzA0NjkgQyA2LjE1NjI1IDUuNzUzOTA2IDYuMDc4MTI1IDUuNzkyOTY5IDYuMDI3MzQ0IDUuODE2NDA2IEMgNS45ODA0NjkgNS44MzU5MzggNS44Nzg5MDYgNS44ODY3MTkgNS44MDQ2ODggNS45MjE4NzUgQyA1LjczMDQ2OSA1Ljk1NzAzMSA1LjYxMzI4MSA2LjAxMTcxOSA1LjU0Njg3NSA2LjA0Mjk2OSBDIDUuNDg0Mzc1IDYuMDc4MTI1IDUuMzcxMDk0IDYuMTI4OTA2IDUuMzA0Njg4IDYuMTY0MDYyIEMgNS4yMzQzNzUgNi4xOTUzMTIgNS4xMzI4MTIgNi4yNDIxODggNS4wNzgxMjUgNi4yNjk1MzEgQyA1LjAyNzM0NCA2LjI5Mjk2OSA0LjkzMzU5NCA2LjMzNTkzOCA0Ljg3ODkwNiA2LjM2MzI4MSBDIDQuODIwMzEyIDYuMzkwNjI1IDQuNzE0ODQ0IDYuNDQxNDA2IDQuNjQ0NTMxIDYuNDc2NTYyIEMgNC40MTAxNTYgNi41ODU5MzggNC4yOTY4NzUgNi42NDA2MjUgNC4xNTIzNDQgNi43MTA5MzggQyA0LjA3NDIxOSA2Ljc0NjA5NCAzLjk2NDg0NCA2Ljc5Njg3NSAzLjkxMDE1NiA2LjgyNDIxOSBDIDMuODU5Mzc1IDYuODUxNTYyIDMuNzYxNzE5IDYuODk4NDM4IDMuNjk1MzEyIDYuOTI1NzgxIEMgMy42MzI4MTIgNi45NTcwMzEgMy41MjczNDQgNy4wMDc4MTIgMy40Njg3NSA3LjAzNTE1NiBDIDMuNDA2MjUgNy4wNjY0MDYgMy4yOTY4NzUgNy4xMTcxODggMy4yMzA0NjkgNy4xNDg0MzggQyAzLjE2MDE1NiA3LjE4MzU5NCAzLjA1MDc4MSA3LjIzNDM3NSAyLjk4NDM3NSA3LjI2NTYyNSBDIDIuOTE3OTY5IDcuMjk2ODc1IDIuODEyNSA3LjM0NzY1NiAyLjc1IDcuMzc4OTA2IEMgMi42MDE1NjIgNy40NDkyMTkgMi4zNTkzNzUgNy41NjY0MDYgMi4xNzU3ODEgNy42NTIzNDQgTCAyLjAzMTI1IDcuNzE4NzUgTCAyLjAzMTI1IDExLjc1NzgxMiBMIDIuMDkzNzUgMTEuNzg1MTU2IEMgMi4xMjUgMTEuODAwNzgxIDIuMjIyNjU2IDExLjg0NzY1NiAyLjMwMDc4MSAxMS44ODY3MTkgQyAyLjM4MjgxMiAxMS45MjE4NzUgMi40ODgyODEgMTEuOTcyNjU2IDIuNTMxMjUgMTEuOTk2MDk0IEMgMi41NzQyMTkgMTIuMDE1NjI1IDIuNjc1NzgxIDEyLjA2MjUgMi43NTM5MDYgMTIuMTAxNTYyIEMgMi44MzIwMzEgMTIuMTM2NzE5IDIuOTQ1MzEyIDEyLjE5MTQwNiAzLjAwNzgxMiAxMi4yMTg3NSBDIDMuMDY2NDA2IDEyLjI1IDMuMTg3NSAxMi4zMDg1OTQgMy4yNzczNDQgMTIuMzUxNTYyIEMgMy4zNjcxODggMTIuMzk0NTMxIDMuNDQxNDA2IDEyLjQyNTc4MSAzLjQ0MTQwNiAxMi40MjU3ODEgQyAzLjQ0NTMxMiAxMi40MjU3ODEgMy41MzEyNSAxMi40Njg3NSAzLjYzMjgxMiAxMi41MTk1MzEgQyAzLjczODI4MSAxMi41NzAzMTIgMy44NjcxODggMTIuNjMyODEyIDMuOTIxODc1IDEyLjY1NjI1IEMgMy45NzY1NjIgMTIuNjgzNTk0IDQuMDg1OTM4IDEyLjczNDM3NSA0LjE2Nzk2OSAxMi43NzM0MzggQyA0LjI1IDEyLjgxMjUgNC4zNTU0NjkgMTIuODYzMjgxIDQuNDAyMzQ0IDEyLjg4NjcxOSBDIDQuNDQ5MjE5IDEyLjkxMDE1NiA0LjU1NDY4OCAxMi45NTcwMzEgNC42MzI4MTIgMTIuOTk2MDk0IEMgNC43MTA5MzggMTMuMDMxMjUgNC44MjAzMTIgMTMuMDg1OTM4IDQuODc4OTA2IDEzLjExMzI4MSBDIDQuOTMzNTk0IDEzLjE0MDYyNSA1LjA2MjUgMTMuMTk5MjE5IDUuMTYwMTU2IDEzLjI0NjA5NCBDIDUuMjU3ODEyIDEzLjI5Njg3NSA1LjMzOTg0NCAxMy4zMzIwMzEgNS4zNDM3NSAxMy4zMzIwMzEgQyA1LjM0Mzc1IDEzLjMzMjAzMSA1LjQyNTc4MSAxMy4zNzEwOTQgNS41MjM0MzggMTMuNDE3OTY5IEMgNS42MjEwOTQgMTMuNDY0ODQ0IDUuNzM0Mzc1IDEzLjUxOTUzMSA1Ljc3MzQzOCAxMy41MzkwNjIgQyA1LjgxMjUgMTMuNTU0Njg4IDUuOTE0MDYyIDEzLjYwNTQ2OSA2IDEzLjY0NDUzMSBDIDYuMDg5ODQ0IDEzLjY4NzUgNi4yMDMxMjUgMTMuNzQyMTg4IDYuMjU3ODEyIDEzLjc2OTUzMSBDIDYuMzEyNSAxMy43OTY4NzUgNi40MjE4NzUgMTMuODQ3NjU2IDYuNTAzOTA2IDEzLjg4NjcxOSBDIDYuNTgyMDMxIDEzLjkyNTc4MSA2LjY4MzU5NCAxMy45NzI2NTYgNi43MjY1NjIgMTMuOTkyMTg4IEMgNi43Njk1MzEgMTQuMDExNzE5IDYuODYzMjgxIDE0LjA1ODU5NCA2LjkzNzUgMTQuMDkzNzUgQyA3LjAxNTYyNSAxNC4xMzI4MTIgNy4xMjEwOTQgMTQuMTgzNTk0IDcuMTc5Njg4IDE0LjIxMDkzOCBDIDcuMjM0Mzc1IDE0LjIzNDM3NSA3LjMzOTg0NCAxNC4yODUxNTYgNy40MTAxNTYgMTQuMzIwMzEyIEMgNy40NzY1NjIgMTQuMzUxNTYyIDcuNTc0MjE5IDE0LjM5ODQzOCA3LjYyNSAxNC40MjE4NzUgQyA3LjY3OTY4OCAxNC40NDUzMTIgNy43ODEyNSAxNC40OTYwOTQgNy44NTU0NjkgMTQuNTMxMjUgQyA3LjkyOTY4OCAxNC41NjY0MDYgOC4wMzkwNjIgMTQuNjE3MTg4IDguMDk3NjU2IDE0LjY0NDUzMSBDIDguMTUyMzQ0IDE0LjY3MTg3NSA4LjI2NTYyNSAxNC43MjY1NjIgOC4zMzk4NDQgMTQuNzYxNzE5IEMgOC40MjE4NzUgMTQuODAwNzgxIDguNTE5NTMxIDE0Ljg0NzY1NiA4LjU1ODU5NCAxNC44NjcxODggQyA4LjYwMTU2MiAxNC44ODY3MTkgOC43MDMxMjUgMTQuOTMzNTk0IDguNzg5MDYyIDE0Ljk3NjU2MiBDIDguODcxMDk0IDE1LjAxNTYyNSA4Ljk4MDQ2OSAxNS4wNjY0MDYgOS4wMjczNDQgMTUuMDg5ODQ0IEMgOS4wNzgxMjUgMTUuMTEzMjgxIDkuMTc5Njg4IDE1LjE2MDE1NiA5LjI1NzgxMiAxNS4xOTkyMTkgQyA5LjMzNTkzOCAxNS4yMzQzNzUgOS40NDkyMTkgMTUuMjg5MDYyIDkuNTA3ODEyIDE1LjMyMDMxMiBDIDkuNTcwMzEyIDE1LjM0NzY1NiA5LjY3NTc4MSAxNS4zOTg0MzggOS43NDIxODggMTUuNDI5Njg4IEMgOS45MTc5NjkgMTUuNTE1NjI1IDEwLjUgMTUuNzg5MDYyIDEwLjY0ODQzOCAxNS44NjMyODEgQyAxMC43MTg3NSAxNS44OTQ1MzEgMTAuODA4NTk0IDE1LjkzNzUgMTAuODQ3NjU2IDE1Ljk1NzAzMSBDIDEwLjkzMzU5NCAxNi4wMDM5MDYgMTAuOTMzNTk0IDE2IDEwLjgyODEyNSAxNS44Nzg5MDYgQyAxMC43OTI5NjkgMTUuODM5ODQ0IDEwLjY4NzUgMTUuNzE4NzUgMTAuNTkzNzUgMTUuNjEzMjgxIEMgMTAuNTAzOTA2IDE1LjUwNzgxMiAxMC40MDYyNSAxNS4zOTQ1MzEgMTAuMzc1IDE1LjM2MzI4MSBDIDEwLjM0NzY1NiAxNS4zMjgxMjUgMTAuMzA0Njg4IDE1LjI4MTI1IDEwLjI4MTI1IDE1LjI1MzkwNiBDIDEwLjI1NzgxMiAxNS4yMjY1NjIgMTAuMjMwNDY5IDE1LjE5NTMxMiAxMC4yMTg3NSAxNS4xODM1OTQgQyAxMC4yMDcwMzEgMTUuMTY3OTY5IDEwLjE3MTg3NSAxNS4xMjg5MDYgMTAuMTQwNjI1IDE1LjA5Mzc1IEMgOS45NTcwMzEgMTQuODgyODEyIDkuODQ3NjU2IDE0Ljc1NzgxMiA5LjgzOTg0NCAxNC43NSBDIDkuODM5ODQ0IDE0Ljc1IDkuNzg5MDYyIDE0LjY5MTQwNiA5LjczNDM3NSAxNC42MjUgQyA5LjY3NTc4MSAxNC41NTg1OTQgOS42MTMyODEgMTQuNDg4MjgxIDkuNTkzNzUgMTQuNDY4NzUgQyA5LjU3ODEyNSAxNC40NDkyMTkgOS40MTc5NjkgMTQuMjY1NjI1IDkuMjQyMTg4IDE0LjA2MjUgQyA5LjA2NjQwNiAxMy44NjMyODEgOC45MTAxNTYgMTMuNjgzNTk0IDguODk0NTMxIDEzLjY2Nzk2OSBDIDguODc4OTA2IDEzLjY0ODQzOCA4LjgzMjAzMSAxMy41OTM3NSA4Ljc4OTA2MiAxMy41NDY4NzUgQyA4Ljc0NjA5NCAxMy41IDguNzEwOTM4IDEzLjQ1NzAzMSA4LjcwNzAzMSAxMy40NTMxMjUgQyA4LjcwMzEyNSAxMy40NDkyMTkgOC42NzU3ODEgMTMuNDE3OTY5IDguNjQwNjI1IDEzLjM3ODkwNiBDIDguNjA5Mzc1IDEzLjMzNTkzOCA4LjU3ODEyNSAxMy4zMDQ2ODggOC41NzQyMTkgMTMuMzAwNzgxIEMgOC41NzAzMTIgMTMuMjk2ODc1IDguNDg0Mzc1IDEzLjE5NTMxMiA4LjM3ODkwNiAxMy4wNzgxMjUgQyA4LjI3MzQzOCAxMi45NTcwMzEgOC4xODc1IDEyLjg1NTQ2OSA4LjE4MzU5NCAxMi44NTE1NjIgQyA4LjE3OTY4OCAxMi44NTE1NjIgOC4wOTc2NTYgMTIuNzUzOTA2IDcuOTk2MDk0IDEyLjY0MDYyNSBDIDcuODk4NDM4IDEyLjUyNzM0NCA3LjgwMDc4MSAxMi40MTQwNjIgNy43ODUxNTYgMTIuMzk0NTMxIEMgNy43NjU2MjUgMTIuMzc1IDcuNjI1IDEyLjIxNDg0NCA3LjQ3MjY1NiAxMi4wMzkwNjIgQyA3LjMyNDIxOSAxMS44NjcxODggNy4xODM1OTQgMTEuNzA3MDMxIDcuMTY0MDYyIDExLjY4NzUgQyA3LjE0NDUzMSAxMS42NjQwNjIgNy4wOTc2NTYgMTEuNjA5Mzc1IDcuMDU4NTk0IDExLjU2NjQwNiBDIDcuMDE5NTMxIDExLjUxOTUzMSA2Ljk4ODI4MSAxMS40ODA0NjkgNi45ODQzNzUgMTEuNDc2NTYyIEMgNi45ODA0NjkgMTEuNDc2NTYyIDYuOTI5Njg4IDExLjQxNzk2OSA2Ljg3NSAxMS4zNTE1NjIgQyA2LjgxNjQwNiAxMS4yODkwNjIgNi43NjE3MTkgMTEuMjIyNjU2IDYuNzUgMTEuMjEwOTM4IEMgNi43MzgyODEgMTEuMTk5MjE5IDYuNzE0ODQ0IDExLjE3MTg3NSA2LjY5OTIxOSAxMS4xNTYyNSBDIDYuNjEzMjgxIDExLjA1NDY4OCA2LjQ2NDg0NCAxMC44ODI4MTIgNi40NjA5MzggMTAuODc4OTA2IEMgNi40NTcwMzEgMTAuODc1IDYuNDIxODc1IDEwLjgzNTkzOCA2LjM4MjgxMiAxMC43OTI5NjkgQyA2LjM0Mzc1IDEwLjc0NjA5NCA2LjMwODU5NCAxMC43MDcwMzEgNi4zMDQ2ODggMTAuNzAzMTI1IEMgNi4zMDQ2ODggMTAuNjk5MjE5IDYuMjY5NTMxIDEwLjY2MDE1NiA2LjIzMDQ2OSAxMC42MTcxODggQyA2LjE5MTQwNiAxMC41NzAzMTIgNi4xNTYyNSAxMC41MjczNDQgNi4xNDg0MzggMTAuNTIzNDM4IEMgNi4xMzY3MTkgMTAuNTExNzE5IDYuMDMxMjUgMTAuMzkwNjI1IDUuOTk2MDk0IDEwLjM1MTU2MiBDIDUuOTYwOTM4IDEwLjMwODU5NCA1Ljk0MTQwNiAxMC4yODUxNTYgNS44ODY3MTkgMTAuMjIyNjU2IEMgNS44MjQyMTkgMTAuMTUyMzQ0IDUuODIwMzEyIDEwLjE0ODQzOCA1LjYyMTA5NCA5LjkyMTg3NSBMIDUuNDY0ODQ0IDkuNzQyMTg4IEwgNS42MzY3MTkgOS42NjAxNTYgQyA1Ljg0NzY1NiA5LjU1ODU5NCA1LjkzNzUgOS41MTk1MzEgNS45NDUzMTIgOS41MTk1MzEgQyA1Ljk0OTIxOSA5LjUxOTUzMSA1Ljk2ODc1IDkuNTA3ODEyIDUuOTg4MjgxIDkuNDk2MDk0IEMgNi4wMDM5MDYgOS40ODA0NjkgNi4wMjM0MzggOS40NzI2NTYgNi4wMjczNDQgOS40NzI2NTYgQyA2LjAzNTE1NiA5LjQ3MjY1NiA2LjEyODkwNiA5LjQyNTc4MSA2LjMzMjAzMSA5LjMyODEyNSBDIDYuNjA1NDY5IDkuMTk5MjE5IDYuNzAzMTI1IDkuMTUyMzQ0IDYuODA0Njg4IDkuMTA1NDY5IEMgNi45MDYyNSA5LjA1ODU5NCA3LjA2MjUgOC45ODA0NjkgNy4yNzczNDQgOC44Nzg5MDYgQyA3LjM0NzY1NiA4Ljg0Mzc1IDcuNDU3MDMxIDguNzkyOTY5IDcuNTE5NTMxIDguNzYxNzE5IEMgNy41ODU5MzggOC43MzA0NjkgNy42OTE0MDYgOC42ODM1OTQgNy43NTM5MDYgOC42NTIzNDQgQyA3LjgyMDMxMiA4LjYyMTA5NCA3LjkxNzk2OSA4LjU3NDIxOSA3Ljk2ODc1IDguNTQ2ODc1IEMgOC4wMjM0MzggOC41MjM0MzggOC4xMjg5MDYgOC40NzI2NTYgOC4yMDcwMzEgOC40Mzc1IEMgOC40NDUzMTIgOC4zMjAzMTIgOC41NzgxMjUgOC4yNTc4MTIgOC42Nzk2ODggOC4yMTA5MzggQyA4LjczNDM3NSA4LjE4MzU5NCA4Ljg0NzY1NiA4LjEzMjgxMiA4LjkyOTY4OCA4LjA4OTg0NCBDIDkuMDE1NjI1IDguMDUwNzgxIDkuMTIxMDk0IDggOS4xNzE4NzUgNy45NzY1NjIgQyA5LjI1MzkwNiA3LjkzNzUgOS4zNDc2NTYgNy44OTA2MjUgOS42NDQ1MzEgNy43NSBDIDkuNzE0ODQ0IDcuNzE4NzUgOS44MTY0MDYgNy42Njc5NjkgOS44NjcxODggNy42NDQ1MzEgQyA5Ljk5MjE4OCA3LjU4NTkzOCAxMC4xNzE4NzUgNy41IDEwLjMyMDMxMiA3LjQyOTY4OCBDIDEwLjQ2MDkzOCA3LjM2MzI4MSAxMC42NDg0MzggNy4yNzM0MzggMTAuNzk2ODc1IDcuMjAzMTI1IEMgMTAuOTM3NSA3LjEzMjgxMiAxMS4wOTM3NSA3LjA1ODU5NCAxMS4yNSA2Ljk4NDM3NSBDIDExLjMxNjQwNiA2Ljk1MzEyNSAxMS40ODQzNzUgNi44NzUgMTEuNjEzMjgxIDYuODEyNSBDIDExLjk4ODI4MSA2LjYzMjgxMiAxMi4wODk4NDQgNi41ODIwMzEgMTIuMzA4NTk0IDYuNDgwNDY5IEMgMTIuNDE3OTY5IDYuNDI5Njg4IDEyLjU5Mzc1IDYuMzQ3NjU2IDEyLjY5NTMxMiA2LjI5Njg3NSBDIDEyLjc5Njg3NSA2LjI0NjA5NCAxMi44Nzg5MDYgNi4yMDcwMzEgMTIuODc4OTA2IDYuMjA3MDMxIEMgMTIuODgyODEyIDYuMjA3MDMxIDEyLjk3MjY1NiA2LjE2NDA2MiAxMy4wODIwMzEgNi4xMDkzNzUgQyAxMy4xOTUzMTIgNi4wNTg1OTQgMTMuMzIwMzEyIDUuOTk2MDk0IDEzLjM2NzE4OCA1Ljk3NjU2MiBDIDEzLjQxMDE1NiA1Ljk1NzAzMSAxMy41MTk1MzEgNS45MDIzNDQgMTMuNjA1NDY5IDUuODYzMjgxIEMgMTMuNjk1MzEyIDUuODIwMzEyIDEzLjgwODU5NCA1Ljc2NTYyNSAxMy44NjcxODggNS43MzgyODEgTCAxMy45Njg3NSA1LjY5MTQwNiBMIDEzLjc4MTI1IDUuNjAxNTYyIEMgMTMuNjc1NzgxIDUuNTUwNzgxIDEzLjU4OTg0NCA1LjUxMTcxOSAxMy41ODk4NDQgNS41MTE3MTkgQyAxMy41ODU5MzggNS41MTE3MTkgMTMuNDg0Mzc1IDUuNDYwOTM4IDEzLjM1OTM3NSA1LjQwMjM0NCBDIDEzLjIzNDM3NSA1LjMzOTg0NCAxMy4xMzI4MTIgNS4yOTI5NjkgMTMuMTMyODEyIDUuMjkyOTY5IEMgMTMuMTI4OTA2IDUuMjkyOTY5IDEzLjA0Njg3NSA1LjI1MzkwNiAxMi45NDUzMTIgNS4yMDMxMjUgQyAxMi44NDM3NSA1LjE1NjI1IDEyLjcxNDg0NCA1LjA5Mzc1IDEyLjY1NjI1IDUuMDY2NDA2IEMgMTIuNTQ2ODc1IDUuMDE1NjI1IDEyLjM4NjcxOSA0LjkzNzUgMTIuMTgzNTk0IDQuODM5ODQ0IEMgMTIuMTE3MTg4IDQuODA4NTk0IDEyLjAyMzQzOCA0Ljc2NTYyNSAxMS45ODA0NjkgNC43NDIxODggQyAxMS45Mzc1IDQuNzIyNjU2IDExLjgxNjQwNiA0LjY2NDA2MiAxMS43MTQ4NDQgNC42MTcxODggQyAxMS42MTMyODEgNC41NjY0MDYgMTEuNSA0LjUxMTcxOSAxMS40NjA5MzggNC40OTYwOTQgQyAxMS4zOTg0MzggNC40NjQ4NDQgMTEuMjUgNC4zOTQ1MzEgMTEuMDA3ODEyIDQuMjgxMjUgQyAxMC45NDE0MDYgNC4yNDYwOTQgMTAuODQzNzUgNC4xOTkyMTkgMTAuNzkyOTY5IDQuMTc1NzgxIEMgMTAuNzM4MjgxIDQuMTUyMzQ0IDEwLjYzNjcxOSA0LjEwMTU2MiAxMC41NTQ2ODggNC4wNjI1IEMgMTAuNDgwNDY5IDQuMDI3MzQ0IDEwLjM3MTA5NCAzLjk3NjU2MiAxMC4zMTY0MDYgMy45NDkyMTkgQyAxMC4yNjE3MTkgMy45MjU3ODEgMTAuMTYwMTU2IDMuODc1IDEwLjA5Mzc1IDMuODQzNzUgQyAxMC4wMjM0MzggMy44MDg1OTQgOS45MTc5NjkgMy43NjE3MTkgOS44NTkzNzUgMy43MzA0NjkgQyA5Ljc5Njg3NSAzLjcwMzEyNSA5LjY4NzUgMy42NDg0MzggOS42MDU0NjkgMy42MTMyODEgQyA5LjQ3MjY1NiAzLjU0Njg3NSA5LjM5ODQzOCAzLjUxMTcxOSA5LjE2NDA2MiAzLjQwMjM0NCBDIDkuMTA5Mzc1IDMuMzc1IDkgMy4zMjAzMTIgOC45MTc5NjkgMy4yODUxNTYgQyA4Ljg0Mzc1IDMuMjQ2MDk0IDguNzM0Mzc1IDMuMTk1MzEyIDguNjc5Njg4IDMuMTY3OTY5IEMgOC42MjUgMy4xNDQ1MzEgOC41MzEyNSAzLjA5NzY1NiA4LjQ2ODc1IDMuMDY2NDA2IEMgOC4zNDc2NTYgMy4wMTE3MTkgOC4xODc1IDIuOTMzNTk0IDguMDAzOTA2IDIuODQ3NjU2IEMgNy44OTQ1MzEgMi43OTY4NzUgNy43NjE3MTkgMi43MzQzNzUgNy41MDc4MTIgMi42MDkzNzUgQyA3LjM1MTU2MiAyLjUzNTE1NiA3LjE5OTIxOSAyLjQ2MDkzOCA3LjA1NDY4OCAyLjM5NDUzMSBDIDcgMi4zNzEwOTQgNi44OTg0MzggMi4zMjAzMTIgNi44MjQyMTkgMi4yODUxNTYgQyA2LjY2MDE1NiAyLjIwNzAzMSA2LjQ5NjA5NCAyLjEyODkwNiA2LjM1NTQ2OSAyLjA2MjUgQyA2LjI5Njg3NSAyLjAzNTE1NiA2LjE4MzU5NCAxLjk4MDQ2OSA2LjEwNTQ2OSAxLjk0MTQwNiBDIDYuMDI3MzQ0IDEuOTA2MjUgNS45MjE4NzUgMS44NTU0NjkgNS44NzUgMS44MzIwMzEgQyA1LjgyODEyNSAxLjgwODU5NCA1LjcyNjU2MiAxLjc2MTcxOSA1LjY0NDUzMSAxLjcyMjY1NiBDIDUuNTcwMzEyIDEuNjg3NSA1LjQ2NDg0NCAxLjYzNjcxOSA1LjQxNzk2OSAxLjYxMzI4MSBDIDUuMzcxMDk0IDEuNTkzNzUgNS4yNDIxODggMS41MzEyNSA1LjEzNjcxOSAxLjQ4MDQ2OSBDIDUuMDI3MzQ0IDEuNDI5Njg4IDQuOTM3NSAxLjM4NjcxOSA0LjkzNzUgMS4zODY3MTkgQyA0LjkzMzU5NCAxLjM4NjcxOSA0LjgzMjAzMSAxLjMzNTkzOCA0LjcwNzAzMSAxLjI3NzM0NCBDIDQuNTgyMDMxIDEuMjE0ODQ0IDQuNDgwNDY5IDEuMTY3OTY5IDQuNDgwNDY5IDEuMTY3OTY5IEMgNC40NzY1NjIgMS4xNjc5NjkgNC4zOTA2MjUgMS4xMjUgNC4yODUxNTYgMS4wNzQyMTkgQyA0LjE4MzU5NCAxLjAyNzM0NCA0LjA0Njg3NSAwLjk2MDkzOCAzLjk4ODI4MSAwLjkzMzU5NCBDIDMuOTI5Njg4IDAuOTA2MjUgMy44MjgxMjUgMC44NTU0NjkgMy43NjU2MjUgMC44MjQyMTkgQyAzLjY5OTIxOSAwLjc5Njg3NSAzLjU5NzY1NiAwLjc0NjA5NCAzLjUzNTE1NiAwLjcxODc1IEMgMy4zNjcxODggMC42MzY3MTkgMy4xOTkyMTkgMC41NTg1OTQgMy4wNTA3ODEgMC40ODQzNzUgQyAyLjk3NjU2MiAwLjQ1MzEyNSAyLjgyODEyNSAwLjM3ODkwNiAyLjcxODc1IDAuMzI4MTI1IEMgMi42MDU0NjkgMC4yNzM0MzggMi40NDE0MDYgMC4xOTUzMTIgMi4zNTE1NjIgMC4xNTIzNDQgQyAyLjI2MTcxOSAwLjEwOTM3NSAyLjE2MDE1NiAwLjA2MjUgMi4xMjg5MDYgMC4wNDY4NzUgQyAyLjA5Mzc1IDAuMDMxMjUgMi4wNTg1OTQgMC4wMTU2MjUgMi4wNTA3ODEgMC4wMDc4MTI1IEMgMi4wMzEyNSAwIDIuMDMxMjUgMC4xMjUgMi4wMzEyNSAyLjU1ODU5NCBaIE0gMi4wMzEyNSAyLjU1ODU5NCAiLz4KPC9nPgo8L3N2Zz4K')
print('---')
print(f'Open profile | href=https://www.rolimons.com/player/{user_id} | key=CmdOrCtrl+o')

"""Offline structural checks only; no imports of controller code or hardware access."""
from pathlib import Path
import ast
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
py_files = list((root / "ros2_ws" / "src").rglob("*.py"))
xml_files = list((root / "ros2_ws" / "src").rglob("package.xml"))
urdf_files = list((root / "ros2_ws" / "src").rglob("*.urdf"))
assert py_files and xml_files, "Source workspace is empty"
for path in py_files:
    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
for path in xml_files + urdf_files:
    ET.parse(path)
print(f"PASS: {len(py_files)} Python files, {len(xml_files)} package manifests, {len(urdf_files)} URDF files")
print("Syntax and XML only. ROS build, asset completeness and hardware behavior are unverified.")

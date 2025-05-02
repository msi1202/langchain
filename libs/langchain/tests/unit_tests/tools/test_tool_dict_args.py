import json
import pytest

from langchain_core.tools.base import BaseTool
def test_tool_accepts_dict_input_and_json_string():
    class EchoTool(BaseTool):
        name = "echo"
        description = "Echo numbers"
        args_schema = {"x": {"type": "number"}, "y": {"type": "number"}}

        def _run(self, x: int, y: int) -> str:
            return f"{x}+{y}={x+y}"

    tool = EchoTool()

    # Direct dict
    assert tool.run({"x": 2, "y": 3}) == "2+3=5"

    # JSON-encoded dict string
    assert tool.run('{"x": 4, "y": 5}') == "4+5=9"

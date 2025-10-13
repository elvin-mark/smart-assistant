from langchain.tools import tool
import numexpr as ne

@tool("calculator")
def calculator(expression: str) -> str:
    """Evaluate (calculate) any math expression

    Args:
        expression: valid math expression
    """
    try:
        result = ne.evaluate(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
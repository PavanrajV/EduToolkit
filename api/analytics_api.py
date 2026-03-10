from flask import Blueprint, jsonify
from database.models import ToolUsage

analytics_api = Blueprint("analytics_api",__name__)

@analytics_api.route("/api/tool-usage")
def usage():

    data = {}

    tools = ToolUsage.query.all()

    for t in tools:
        data[t.tool_name] = data.get(t.tool_name,0) + 1

    return jsonify(data)
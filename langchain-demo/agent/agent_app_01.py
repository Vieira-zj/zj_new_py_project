from typing import List, Optional, TypedDict

from langgraph.graph import END, StateGraph


class AgentState(TypedDict):
    messages: List[str]
    user_intent: Optional[str]
    next_step: Optional[str]


def intent_analysis_agent(state):
    print(f"analysis user intent {state}...")
    return {"user_intent": "repair", "next_step": "dispatch"}


def assistant_reply_agent(state):
    print("💬 generate reply...")
    return {"messages": state["messages"] + ["query results"]}


def dispatch_ticket_agent(state):
    print("dispatch ticket ...")
    # mock api call
    return {"messages": state["messages"] + ["ticket created"]}


def router(state):
    if state["user_intent"] == "repair":
        return "dispatch"
    return "assistant"


def agent_main():
    workflow = StateGraph(AgentState)
    workflow.add_node("intent_analysis", intent_analysis_agent)
    workflow.add_node("assistant_reply", assistant_reply_agent)
    workflow.add_node("dispatch_ticket", dispatch_ticket_agent)

    workflow.set_entry_point("intent_analysis")
    workflow.add_conditional_edges(
        "intent_analysis",
        router,
        {"dispatch": "dispatch_ticket", "assistant": "assistant_reply"},
    )
    workflow.add_edge("assistant_reply", END)
    workflow.add_edge("dispatch_ticket", END)

    app = workflow.compile()
    print("start workflow")
    input_state = AgentState(
        **{"messages": ["my tv is broken"], "user_intent": None, "next_step": None}
    )
    output = app.invoke(input_state)
    print("agent output:", output["messages"])


if __name__ == "__main__":
    agent_main()

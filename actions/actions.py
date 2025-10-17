from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideResources(Action):
    def name(self) -> str:
        return "action_provide_resources"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        dispatcher.utter_message(
            text="Here are some mental health resources:\n"
                 "- 🧘 Calm app: https://www.calm.com\n"
                 "- 💬 7 Cups: https://www.7cups.com\n"
                 "- 📞 Helpline: 1800-599-0019 (India)"
        )
        return []

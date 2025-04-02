class Agent:
    def __init__(self, system="", actions=None):
        self.log = logging.getLogger("main.Agent")
        self.log.info("Initializing Agent")

        # Initialize the messages with the system message
        self.messages = []
        if system:
            self.messages.append({"role": "system", "content": system})
            self.log.debug(f"Agent initialized for system {system}")

        # Initialize the known actions
        self.known_actions = {}
        if actions is not None:
            for action, value in actions.items():
                self.known_actions[action] = value["function"]

        self.max_turns = 10
        self.action_re = re.compile(r'^Action: (\w+): (.*)$')
        self.answer_re = re.compile(r'^Answer: (.*)$')

    def handle_user_message(self, message):
        self.log.info(f"Received message: {message}")
        self.messages.append({"role": "user", "content": message})
        result = self.__execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def __execute(self) -> str:
        response: ChatResponse = chat(
            model=MODEL,
            messages=self.messages,
            options={
                "temperature": 0,
                "stop": [
                    'PAUSE'
                ]
            }
        )
        self.log.info(f"Response: {response.message.content}")
        return response.message.content

    def ask_question(self, question):
        i = 0
        next_prompt = question
        while i < self.max_turns:
            i += 1
            result = self.handle_user_message(next_prompt)

            # Check if there is an action to run or an answer to return
            actions = [self.action_re.match(a) for a in result.split('\n') if self.action_re.match(a)]
            if actions:
                next_prompt = self.__execute_action(actions)
            else:
                return self.__extract_answer(result)

    def __execute_action(self, actions):
        action, action_input = actions[0].groups()
        if action not in self.known_actions:
            main_log.error("Unknown action: %s: %s", action, action_input)
            raise Exception("Unknown action: {}: {}".format(action, action_input))

        main_log.info(" -- running %s %s", action, action_input)
        observation = self.known_actions[action](action_input)

        main_log.info("Observation: %s", observation)
        return f"Observation: {observation}"

    def __extract_answer(self, result):
        answers = [self.answer_re.match(answer) for answer in result.split('\n') if self.answer_re.match(answer)]
        if answers:
            # There is an answer to return
            main_log.info("Final answer: %s", answers[0].groups()[0])
            return answers[0].groups()[0]
        else:
            main_log.error("No action or answer found in: %s", result)
            raise Exception("No action or answer found in: {}".format(result))

    def complete_agent(question=None):
        # Set up the Agent
        meeting_actions = {
            "find_person_availability": {
                "description": "finding a person using the name and returning their availability",
                "function": find_person_availability
            },
            "find_meeting_room_availability": {
                "description": "finding a meeting room using the name and returning its availability",
                "function": find_meeting_room_availability
            }
        }
        system_prompt = create_system_prompt(meeting_actions)
        bot = Agent(system_prompt, meeting_actions)

        # Ask a question
        final_answer = bot.ask_question(sample_question)
        print("Answer:", final_answer)


    if __name__ == '__main__':
        _ = load_dotenv()
        setup_logging()
        main_log = logging.getLogger("main")
        main_log.setLevel(logging.INFO)
        logging.getLogger("main.Agent").setLevel(logging.INFO)

        sample_question = """I am Jettro, can you book a meeting for me with Daniel and Joey on Monday in Room 3?"""
        complete_agent(sample_question)
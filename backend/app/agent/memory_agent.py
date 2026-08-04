class MemoryAgent:

    def __init__(self):

        pass

    def build(self, messages):

        if not messages:
            return ""

        result = []

        for message in messages:

            sender = getattr(
                message,
                "sender",
                ""
            )

            content = getattr(
                message,
                "content",
                ""
            )

            if content:

                result.append(
                    f"{sender}: {content}"
                )

        return "\n".join(result)
from typing import List, Dict, Union


class BalancedStringAssessment:
    def check_string_is_balanced(
        self,
        input_string: str,
    ) -> bool:
        """
        :param input_string: string containing characters and zero or more symbols
        :return: a boolean value reflecting if input_string is balanced or not
        """
        # TODO: Implement function body
        # build a dictionary of closers to openers
        closers_to_openers = {")": "(", "}": "{", "]": "["}

        # set of openers to compare to while looping
        openers = set(closers_to_openers.values())

        # list of seen openers
        openers_seen = []

        for char in input_string:
            # pushes open characters to openers_seen
            if char in openers:
                openers_seen.append(char)

            # check closing characters, the values of the dictionary
            elif char in closers_to_openers:
                # if there are no opening characters return false
                if not openers_seen:
                    return False

                if openers_seen[-1] == closers_to_openers.get(char):
                    openers_seen.pop()

                else:
                    return False

        return openers_seen == []


class TestBalancedStringAssessment:
    def __init__(self):
        self.balanced_string_assessment = BalancedStringAssessment()

    @staticmethod
    def get_tests() -> List[Dict[str, Union[str, bool]]]:
        tests = [
            {
                "input_string": "[a]{b}(c)",
                "expected_result": True,
            },
            {
                "input_string": "[(ab){c}]",
                "expected_result": True,
            },
            {
                "input_string": "([a)]",
                "expected_result": False,
            },
            {
                "input_string": "(([b])",
                "expected_result": False,
            },
            {
                "input_string": "b)",
                "expected_result": False,
            },
            {
                "input_string": "{c",
                "expected_result": False,
            },
            {
                "input_string": "abc",
                "expected_result": True,
            },
            {
                "input_string": "",
                "expected_result": True,
            },
            {
                "input_string": "[]{}()",
                "expected_result": True,
            },
        ]

        return tests

    def run_individual_test(
        self, index: int, test: Dict[str, Union[str, bool]]
    ) -> bool:
        string_is_balanced_result = (
            self.balanced_string_assessment.check_string_is_balanced(
                test["input_string"]
            )
        )

        test_passed = string_is_balanced_result == test["expected_result"]

        if not test_passed:
            print(f"Test {str(index + 1)} failed!")
            print(f"Input string: {test['input_string']}")
            print(f"Resulting output: {str(string_is_balanced_result)}")
            print(f"Expected output: {str(test['expected_result'])}\n")

        return test_passed

    def test_balanced_string_assessment_solution(self):
        tests = self.get_tests()
        all_tests_passed = all(
            self.run_individual_test(index, test) for index, test in enumerate(tests)
        )
        if all_tests_passed:
            print("Congrats, all tests passed!")


if __name__ == "__main__":
    TestBalancedStringAssessment().test_balanced_string_assessment_solution()
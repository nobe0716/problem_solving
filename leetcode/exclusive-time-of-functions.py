from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        job_stack = []

        execution_times = [0] * n
        for log in logs:
            function_id, operation, timestamp = log.split(':')
            function_id, timestamp = int(function_id), int(timestamp)

            if operation == 'start':
                if job_stack:
                    job_stack[-1][-1] = timestamp - 1
                    execution_times[job_stack[-1][0]] += (job_stack[-1][-1] - job_stack[-1][-2] + 1)
                job_stack.append([function_id, timestamp, 0])
            else:
                _, started_at, _ = job_stack.pop()
                execution_times[function_id] += (timestamp - started_at) + 1
                if job_stack:
                    job_stack[-1][-2] = timestamp + 1

        return execution_times


s = Solution()
assert s.exclusiveTime(n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"]) == [3, 4]
assert s.exclusiveTime(n=1, logs=["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]) == [8]
assert s.exclusiveTime(n=2, logs=["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]) == [7, 1]
assert s.exclusiveTime(n=2, logs=["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]) == [8, 1]
assert s.exclusiveTime(n=1, logs=["0:start:0", "0:end:0"]) == [1]

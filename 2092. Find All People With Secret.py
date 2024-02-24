# 24 POTD 
# Problem: 2092. Find All People With Secret
# Language :  python 
# link: https://leetcode.com/problems/find-all-people-with-secret/submissions/1184973681



class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        visited = [False] * n
        visited[0] = visited[firstPerson] = True

        meetings.sort(key=lambda x: x[2])

        i, total_meetings = 0, len(meetings)
      
        while i < total_meetings:
            j = i
            while j + 1 < total_meetings and meetings[j + 1][2] == meetings[i][2]:
                j += 1
            participants = set()
            connections = defaultdict(list)
          
            for person_a, person_b, _ in meetings[i : j + 1]:
                connections[person_a].append(person_b)
                connections[person_b].append(person_a)
                participants.update([person_a, person_b])
          
            queue = deque([person for person in participants if visited[person]])
          
            while queue:
                current_person = queue.popleft()
                for neighbor in connections[current_person]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
          
            i = j + 1
      
        return [person for person, knows_secret in enumerate(visited) if knows_secret]

import asyncio
import time


class AIRequest:
    def __init__(
        self,
        request_id: int,
        prompt: str,
        model: str,
        estimated_time: float,
        status: str = "pending",
    ) -> None:
        if prompt is None or not prompt.strip():
            raise ValueError("The prompt cannot be empty")

        self.request_id = request_id
        self.prompt = prompt
        self.model = model
        self.estimated_time = estimated_time
        self.status = status


class BatchProcessor:
    def __init__(self, requests: list[AIRequest]) -> None:
        self.requests = requests

    async def process_request(self, request: AIRequest) -> str:
        try:
            request.status = "in progress"
            await asyncio.sleep(request.estimated_time)
            request.status = "completed"
            return f"Request {request.request_id} ({request.model}): success"
        except Exception:
            request.status = "error"
            return f"Request {request.request_id} ({request.model}): processing error"

    async def process_all(self) -> list[str]:
        return await asyncio.gather(
            *(self.process_request(request) for request in self.requests)
        )


async def main() -> None:
    print("Testing the AI request processor...")

    request1 = AIRequest(
        request_id=1,
        prompt="Explain Python",
        model="GPT-4",
        estimated_time=1.5,
    )
    request2 = AIRequest(
        request_id=2,
        prompt="Explain AI",
        model="Claude-3.5",
        estimated_time=2.0,
    )

    processor = BatchProcessor([request1, request2])

    start_time = time.perf_counter()
    results = await processor.process_all()
    end_time = time.perf_counter()

    print("--- Processing results ---")
    for result in results:
        print(result)

    print(f"Total processing time: {end_time - start_time:.2f} seconds")
    print(f"Request 1 status: {request1.status}")
    print(f"Request 2 status: {request2.status}")


if __name__ == "__main__":
    asyncio.run(main())

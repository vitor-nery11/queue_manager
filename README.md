# Gerenciador de fila de requisições

Este projeto demonstra como processar várias requisições de IA de forma assíncrona usando apenas recursos da biblioteca padrão do Python. O processamento é simulado com esperas; nenhuma API de IA é chamada.

## Como funciona

- `RequisicaoIA` representa uma requisição, com identificador, prompt, modelo, tempo estimado e status. O prompt não pode ser vazio.
- `ProcessadorLote` processa cada requisição e atualiza seu status para `em andamento`, `concluido` ou `erro`.
- `processar_todas()` usa `asyncio.gather` para processar as requisições em paralelo.
- A função `main()` cria duas requisições de exemplo, mostra os resultados, o tempo total e os status finais.

## Como executar

No terminal, a partir da pasta do projeto:

```bash
python gerenciador_de_fila.py
```

O tempo total tende a ficar próximo ao da requisição mais demorada, pois as esperas acontecem em paralelo.

---

# AI Request Queue Manager

This project demonstrates how to process multiple AI requests asynchronously using only Python's standard library. Processing is simulated with delays; no AI API is called.

## How it works

- `RequisicaoIA` represents a request with an ID, prompt, model, estimated processing time, and status. The prompt cannot be empty.
- `ProcessadorLote` processes each request and updates its status to `em andamento` (in progress), `concluido` (completed), or `erro` (error).
- `processar_todas()` uses `asyncio.gather` to process requests concurrently.
- The `main()` function creates two example requests, then displays the results, total elapsed time, and final statuses.

## How to run

From the project directory, run:

```bash
python gerenciador_de_fila.py
```

The total time should be close to that of the slowest request because the simulated delays run concurrently.

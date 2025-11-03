# FastAPI Unity Backend Sample

[![CI](https://github.com/<YOUR_USERNAME>/fastapi-unity-backend-sample/actions/workflows/ci.yml/badge.svg)](https://github.com/<YOUR_USERNAME>/fastapi-unity-backend-sample/actions/workflows/ci.yml)

Production-ready backend for Unity games with JWT auth, state sync, and telemetry.

## Features
- JWT Authentication
- State synchronization
- Telemetry ingestion
- Docker ready
- Unity client example
- Comprehensive tests
- GitHub Actions CI

## Quick Start

```bash
# Local development
uvicorn app.main:app --reload

# Docker
docker-compose up --build
```

## Quick API examples

### 1) Login (get token)
```bash
curl -s -X POST "http://localhost:8000/api/login"   -H "Content-Type: application/json"   -d '{"player_id":"alice"}' | jq
```

### 2) Sync (authenticated)
```bash
TOKEN=$(curl -s -X POST "http://localhost:8000/api/login" -H "Content-Type: application/json" -d '{"player_id":"alice"}' | jq -r .token)

curl -s -X POST "http://localhost:8000/api/sync"   -H "Content-Type: application/json"   -H "Authorization: Bearer $TOKEN"   -d '{"player_id":"alice","state":{"level":1,"score":100}}' | jq
```

### 3) Telemetry
```bash
curl -s -X POST "http://localhost:8000/api/telemetry"   -H "Content-Type: application/json"   -H "Authorization: Bearer $TOKEN"   -d '{"player_id":"alice","event":"jump","payload":{"height":2.3}}' | jq
```

> Note: install `jq` for pretty JSON in examples. Replace `<YOUR_USERNAME>` in the badge URL with your GitHub username.

## API Documentation
- `POST /api/login` - Get JWT token
- `POST /api/sync` - Sync game state (authenticated)
- `POST /api/telemetry` - Send analytics events

## Unity Integration
See `unity_example/UnityClient.cs` for a minimal C# example.

# example 1
curl -d '{"prompt":"Hello, how are you today?"}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:3000

# example 2
curl -d '{"prompt":"Hello, how are you today?","model":"text-davinci-002","temperature":0.5}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:3000

echo "Subindo container"
docker-compose up -d

echo "Aguardando PostgreSQL iniciar..."
sleep 3

echo "Dados iniciais:"
docker exec -it desafio2 psql -U admin -d teste_desafio2 -c "SELECT * FROM usuarios;"

echo ""
echo "Removendo container (volume permanece)"
docker-compose down

echo ""
echo "Subindo novamente para testar persistência"
docker-compose up -d
sleep 3

echo "Dados após recriação (persistência):"
docker exec -it desafio2 psql -U admin -d teste_desafio2 -c "SELECT * FROM usuarios;"

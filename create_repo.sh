source .env

curl -H "Authorization: token $GH_TOKEN" \
     -d '{"name":"research_recommender","description":"Research Paper Recommender","private":false}' \
     https://api.github.com/user/repos

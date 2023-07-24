Technologies used:

kubectl
python (flask)
docker
kubernetes

To setup:
    run docker file:
        docker build -t docker-file .

        docker run docker-file

    run kubernetes:
        kubectl apply -f deployment.yml

        kubectl get deployments (confirm build)

        kubectl get services (confirm running state)

        in browser:
            localhost
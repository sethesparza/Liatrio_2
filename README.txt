Technologies used:

kubectl
python (flask)
docker
kubernetes
AWS



to run application alone:
    in terminal:
        python app.py



To build docker image and test it works:
    run docker file:
        docker build -t docker-file .

        docker run docker-file



run  and deploy kubernetes cluster to AWS:

        aws ecr create-repository --repository-name <name> --region us-east-1

        aws ecr get get-login-password --region us-east-1

        aws ecr --region us-east-1 | docker login -u AWS -p <password> <account_id>.dkr.ecr.us-east-1.amazonaws.com/<repo name>

        docker tag <name>:latest <account_id>.dkr.ecr.us-east-1.amazonaws/<name>:latest

        docker push 

        docker push <ACCOUNTID>.dkr.ecr.us-east-1.amazonaws.com/webapp:latest

        aws cloudformation deploy --template-file <path>/amazon-eks-vpc-private-subnets.yaml --stack-name <name of stack>

        eksctl create cluster -f cluster.yaml --kubeconfig=C:\Users\<user>\.kube\config

        kubectl apply -f deployment.yaml

        kubectl apply -f service.yaml

        kubectl get services

        kubectl get pods -o wide

        kubectl get nodes -o wide

        kubectl get deployments (confirm build)

        kubectl get services (confirm running state)



        in browser:
            localhost
    
        OR

        in browser: 
            external IP (load balancer)

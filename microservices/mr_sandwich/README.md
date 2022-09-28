# Welcome To The Microservices Tutorial Lab
Learning new technologies shouldn't go without some good practise, that's why I'm giving you a fully configured and
production ready system, which will help you better understand Microservices-related concepts.

## Ingredients
As you can see, there are two directories in the root of this tutorial: `specification`, which contains all necessary
documentation, and `src` containing Microservices. This is supposed to be your main workspace, every topic mentioned
in the articles being part of [Microservices](https://szpak.dev/tutorials#microservices) tutorial on the **Information
Technology by Tomasz Szpak**.

## Running The Stack
Everything is already configured and ready to build. To initiate the stack, simply run:

```shell
docker-compose up -d
```

After few minutes everything will be installed and ready to work. Go to `https://localhost/auth/login` and if you can 
see a login form, it means that everything was provisioned successfully.

## What If Something Goes Wrong?
If you have any problems with running the system, just create an Issue and describe your problem. I will do my best to 
answer you as soon as possible.
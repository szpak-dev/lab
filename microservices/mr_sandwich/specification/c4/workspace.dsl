workspace "Mr. Sandwich Food" "Schema of food distributing platform" {
    model {
        customer = person "Customer" "Hungry office worker"

        enterprise "Mr. Sandwich" {
            admin = person "System Admin"
            chef = person "Chef" "Person who cooks Dishes"
            deliverer = person "Deliverer" "Person who delivers dishes to Delivery Point"

            load_balancer = softwareSystem "Load Balancer" {
                customer -> this "Uses"
                admin -> this "Uses"
                chef -> this "Uses"
                deliverer -> this "Uses"
                web_proxy = container "Web Server" {
                    component "Proxy Module" "Responsible for proxying requests to their respective services"
                }
            }

            auth = softwareSystem "Auth Gateway" {
                web_proxy -> this "Passes"
                auth_admin = container "Web App" {
                    component "Users Controller" "Admin manages all Users, can terminate session instantly"
                }
                auth_api = container "Web API" {
                    component "Session Controller" "Everyone log in and out here"
                    component "User Controller" "Allows to fetch logged in User's object"

                }
                auth_proxy = container "Proxy Pass" {
                    component "Proxy Pass Controller" "Authorizes and passes requests to their respective targets"
                }
            }

            food_factory = softwareSystem "Food Factory" {
                auth_proxy -> this "Passes"
                food_factory_web_admin = container "Web App" {
                    component "Ingredients Controller" "Chef manages ingredients"
                    component "Recipes Controller" "Chef creates and improves Recipes"
                    component "Dishes Controller" "Chef create and edit Dishes"
                }
                food_factory_api = container "Web API" {
                    component "Reservation Controller" "Since there is limited number of Dishes per day, reservations are needed"
                }
                food_factory_db = container "Database" {
                    food_factory_web_admin -> this "Uses"
                    food_factory_api -> this "Uses"
                }
            }

            web_store_cart = softwareSystem "Web Store Cart" {
                auth_proxy -> this "Passes"
                web_store_cart_api = container "Web API" {
                    component "Product Controller" "Customer browse Products list"
                    component "Cart Controller" "Customer manages his Cart"
                }
                web_store_cart_db = container "Database" {
                    web_store_cart_api -> this "Uses"
                }
            }

            delivery = softwareSystem "Delivery" {
                auth_proxy -> this "Passes"
                delivery_web_admin = container "Backend Web App" {
                    component "Route Controller" "Admin manages Routes and add or remove Delivery Points"
                    component "Delivery Point Controller" "Admin manages Delivery Points, resend notifications, sets delivery time"
                    component "Deliverer Controller" "Deliverer checks-in, see his Routes and Delivery Points"
                }
                delivery_mobile_app = container "Mobile App" {
                    component "Routes View" "Deliverer browses his Routes and Delivery Points"
                    component "Delivery Point View" "Deliverer Checks-In"
                    component "Order View" "Deliverer scans Order Id from Customer's smartphone, see ordered products"
                }
                delivery_web_api = container "Web Api" {
                    component "Route Controller" "Deliverer displays his Routes"
                    component "CheckIn Controller" "Deliverer checks-in to Delivery Point, customers are informed about his arrival"
                    component "Order Controller" "Tells if a given Order is a matter of today's Delivery, returns products in Order"
                }
                delivery_db = container "Database" {
                    delivery_web_admin -> this "Uses"
                    delivery_web_api -> this "Uses"
                }
            }
        }
    }

    views {
        styles {
            element "Person" {
                color #ffffff
                fontSize 22
                shape Person
            }
            element "Customer" {
                background #08427b
            }
            element "Bank Staff" {
                background #999999
            }
            element "Software System" {
                background #1168bd
                color #ffffff
            }
            element "Existing System" {
                background #999999
                color #ffffff
            }
            element "Container" {
                background #438dd5
                color #ffffff
            }
            element "Web Browser" {
                shape WebBrowser
            }
            element "Mobile App" {
                shape MobileDeviceLandscape
            }
            element "Database" {
                shape Cylinder
            }
            element "Component" {
                background #85bbf0
                color #000000
            }
            element "Failover" {
                opacity 25
            }
        }
    }
}

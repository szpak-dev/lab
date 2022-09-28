workspace "Mr. Sandwich Food" "Schema of food distributing platform" {
    model {
        customer = person "Customer" "Hungry office worker"

        enterprise "Mr. Sandwich" {
            admin = person "System Admin"
            chef = person "Chef" "Person who cooks Dishes"
            deliverer = person "Deliverer" "Person who delivers dishes to Delivery Point"

            food_factory = softwareSystem "Food Factory" {
                food_factory_web_admin = container "Backend Web App" {
                    admin -> this "Uses"
                    component "Ingredients Controller" "Chef manages ingredients"
                    component "Recipes Controller" "Chef creates and improves Recipes"
                    component "Dishes Controller" "Chef create and edit Dishes"
                }
                food_factory_web_app = container "Web App" {
                    chef -> this "Uses"
                    component "Recipe Controller" "Chef get recipes to know how to cook a Dish"
                    component "Cooking Controller" "Chef registeres every dish produced and packed"
                }
                food_factory_db = container "Database" {
                    food_factory_web_admin -> this "Uses"
                    food_factory_web_app -> this "Uses"
                }
            }

            web_store = softwareSystem "Web Store" {
                web_store_web_admin = container "Backend Web App" {
                    admin -> this "Uses"
                    component "Product Controller" "Create, edit, activate and deactivate products"
                    component "Report Controller" "All required reports are generated here"
                }
                web_store_web_app = container "Web App" {
                    customer -> this "Uses"
                    component "Product Controller" "Customer browse products list"
                    component "Cart Controller" "Customer manages his Cart"
                    component "Order Controller" "Customer see historical Orders accept or decline Order"
                }
                web_store_db = container "Database" {
                    web_store_web_admin -> this "Uses"
                    web_store_web_app -> this "Uses"
                }
            }

            delivery = softwareSystem "Delivery" {
                delivery_web_admin = container "Backend Web App" {
                    admin -> this "Uses"
                    component "Route Controller" "Admin manages Routes and add or remove Delivery Points"
                    component "Delivery Point Controller" "Admin manages Delivery Points, resend notifications, sets delivery time"
                    component "Deliverer Controller" "Deliverer checks-in, see his Routes and Delivery Points"
                }
                delivery_mobile_app = container "Mobile App" {
                    deliverer -> this "Uses"
                    component "Routes View" "Deliverer browses his Routes and Delivery Points"
                    component "Delivery Point View" "Deliverer Checks-In"
                    component "Order View" "Deliverer scans Order Id from Customer's smartphone, see ordered products"
                }
                delivery_web_api = container "Web Api" {
                    delivery_mobile_app -> this "Uses"
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

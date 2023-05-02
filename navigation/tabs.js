import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import {Home} from '../screen/home'
import { QrCodeScreen } from "../screen/qr-code-scren";
import { Ionicons } from "@expo/vector-icons";
import { ListaStack } from "./stack";
import { ListaProducto } from "../screen/ventas/nota-ventas";
import { Carrito } from "../screen/carrito";
const Tab = createBottomTabNavigator();

export  const HomeTabs=()=>{
    return(
        <Tab.Navigator 
        screenOptions={({route})=>({
            headerShown:false,
            tabBarShowLabel:false,
            tabBarStyle:{backgroundColor:'black'},
            tabBarActiveTintColor:'green',
            // tabBarInactiveTintColor:'red',
            tabBarIcon:({focused,color,size})=>{
                let iconName;
                if(route.name==='HomeTabs'){
                    iconName=focused?'home':'home-outline'
                }
                else if(route.name==='QrCode'){
                    iconName=focused?'qr-code':'qr-code-outline'
                }
                return <Ionicons name={iconName} size={focused? 35:size} color={color}/>
            }
            
        })}
        >
            <Tab.Screen 
            name="HomeTabs" 
            component={Home}
            options={{title:'Home'}}
            />
            <Tab.Screen name="QrCode" component={QrCodeScreen}/>
        </Tab.Navigator>
    );
}
export  const ProducTabs=()=>{
    return(
        <Tab.Navigator 
        screenOptions={({route})=>({
            headerShown:false,
            tabBarShowLabel:false,
            tabBarStyle:{backgroundColor:'black'},
            tabBarActiveTintColor:'green',
            // tabBarInactiveTintColor:'red',
            tabBarIcon:({focused,color,size})=>{
                let iconName;
                if(route.name==='HomeTabs'){
                    iconName=focused?'toggle':'toggle-outline'
                }
                else if(route.name==='Carrito'){
                    iconName=focused?'cart':'cart-outline'
                }
                return <Ionicons name={iconName} size={focused? 35:size} color={color}/>
            }
            
        })}
        >
            <Tab.Screen 
            name="HomeTabs" 
            component={ListaProducto}
            options={{title:'Home',headerTitleAlign:'center'}}
            />
            <Tab.Screen 
            name="Carrito" 
            component={Carrito}
            options={{title:'Carrito'}}
            />
            
        </Tab.Navigator>
    );
}

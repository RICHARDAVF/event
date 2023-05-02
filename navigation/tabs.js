import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import {Home} from '../screen/home'
import { QrCodeScreen } from "../screen/qr-code-scren";
import { Ionicons } from "@expo/vector-icons";
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
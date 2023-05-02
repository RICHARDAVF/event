import { createStackNavigator } from "@react-navigation/stack";
import { Detail } from "../screen/details";
import { navOptions } from "./options";
import { useNavigation } from "@react-navigation/native";
import { ProfileDetail } from "../screen/profiles/profile-detail";
import { ProfileScreen } from "../screen/profiles/profiles-screen";
import { ListaProducto } from "../screen/ventas/nota-ventas";
import { HomeTabs } from "./tabs";

const Stack = createStackNavigator();

export const HomeStack =()=>{
    const navigation  = useNavigation();
    return(
        <Stack.Navigator screenOptions={()=>navOptions(navigation)}>
            <Stack.Screen name="Home" component={HomeTabs}/>
        </Stack.Navigator>
    );
}
export const ListaStack=()=> {
    const navigation  = useNavigation();

    return (
        <Stack.Navigator screenOptions={()=>navOptions(navigation)}>
            <Stack.Screen name="Lista" component={ListaProducto} options={{title:'Lista de productos',headerTitleAlign:'center'}}/>
            <Stack.Screen name="Event" component={Detail} />
        </Stack.Navigator>
    );
}

export const ProfileStack=()=> {
    const navigation  = useNavigation()
    return (
        <Stack.Navigator screenOptions={()=>navOptions(navigation)}>
            <Stack.Screen name="ProfileScreen" component={ProfileScreen} />
            <Stack.Screen name="ProfileDetail" component={ProfileDetail} />
        </Stack.Navigator>
    );
}


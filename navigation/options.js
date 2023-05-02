import { Ionicons } from "@expo/vector-icons";
export const navOptions = (nav)=>{
    return{
        headerTintColor:'#cbd5e1',
        headerStyle:{
            backgroundColor:'#0f172a'
        },
        headerRight:()=>(
            <Ionicons
            name="menu"
            size={32}
            color="white"
            onPress={()=>nav.toggleDrawer()}
            />
        ),
        
        
       
    };
}
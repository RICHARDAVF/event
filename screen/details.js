import  {useNavigation, useRoute} from '@react-navigation/native'
import { useLayoutEffect } from 'react';
import { View,StyleSheet ,Text} from "react-native";


export const Detail =() => {
    const route = useRoute();
    const navigation  = useNavigation();
    const {eventId} = route.params;
    
    useLayoutEffect(()=>{
        navigation.setOptions({
            headerTitle:'Producto Seleccionado',
            headerTitleAlign:'center'
            
            
        })
    },[])
    return(
        <View style={styles.home}>
            <Text>Elemento seleccionado {eventId}</Text>
        </View>
    )
    
}
const styles = StyleSheet.create({
    home:{
        padding:20
    }
})
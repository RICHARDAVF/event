import  {useNavigation, useRoute} from '@react-navigation/native'
import { useLayoutEffect } from 'react';
import { View,StyleSheet ,Button } from "react-native";


export const ProfileScreen =() => {
 
    const navigation  = useNavigation();
    
    useLayoutEffect(()=>{
        navigation.setOptions({
            title:'Profile'
           
        })
    })
    return(
        <View style={styles.home}>
           <Button title='Presme' onPress={()=>navigation.navigate('ProfileDetail',{profileId:1})}/>
        </View>
    )
    
}
const styles = StyleSheet.create({
    home:{
        padding:20
    }
})
import  {useNavigation, useRoute} from '@react-navigation/native'
import {HeaderBackButton} from '@react-navigation/elements';
import { useLayoutEffect } from 'react';
import { View,StyleSheet ,Text} from "react-native";


export const ProfileDetail =() => {
    const route = useRoute();
    const navigation  = useNavigation();
    const {profileId} = route.params;
    useLayoutEffect(()=>{
        navigation.setOptions({
        //    headerleLeft:()=>(
        //     <HeaderBackButton
        //         tintColor='white'
        //         onPress={()=>navigation.goBack()}
        //     />
        //    )
        });
    },[])
    return(
        <View style={styles.home}>
            <Text>Elemento seleccionado {profileId}</Text>
        </View>
    )
    
}
const styles = StyleSheet.create({
    home:{
        padding:20
    }
})
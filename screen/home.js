import { StyleSheet } from "react-native";
import { Text, View } from "react-native";
import React, { useContext } from 'react';
import { Contex } from "./context";

export const Home = ()=>{
    const globalContex = useContext(Contex)
    const {usuario} = globalContex;
    return(
        <View style={styles.home}>
            <Text>Home</Text>
            <Text>Hola {usuario}</Text>
        </View>
    );
}
const styles = StyleSheet.create({
    home:{
        flex:1,
        alignContent:'center',
        alignItems:'center',
        justifyContent:'center'
    }
});
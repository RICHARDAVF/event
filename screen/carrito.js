import { useContext } from "react";
import { StyleSheet, View,Text } from "react-native";
import { Contex } from "./context";
export const Carrito = ()=>{
    const  globalContex = useContext(Contex);
    const {productos,setProductos} = globalContex;
    console.log(productos)
    return (
        <View style={styles.container}>
            <Text>Carrito</Text>

        </View>
    );
}
const styles = StyleSheet.create({
    container : {
        fleax:1,
        backgroundColor:'fff1',
        
    }
});
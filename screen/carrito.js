import { StyleSheet, View,TouchableOpacity ,Text} from "react-native";
import { Contex } from "./context";
import { useContext, useEffect, useState } from "react";
export const Carrito = ()=>{
    const  globalContex = useContext(Contex);
    const [sumTotal,setSumTotal] = useState(0);
    const {productos} = globalContex;

    function sumar(){
        var t = 0;
        for (item in productos){
            t+=parseFloat(productos[item].total);
        }
        return t;
      
    }
    const renderItem = productos.map((value,index)=>(
    
        <TouchableOpacity key={index} style={[styles.element,{justifyContent:'space-between',flexDirection:'row',height:30}]} onPress={()=>console.log(index)}>
            <Text style={{width:'30%',textAlign:'center',borderRightWidth:1}}>{value.producto}</Text>
            <Text style={{width:'30%',textAlign:'center',borderRightWidth:1}}>s/ {value.precio}</Text>
            <Text style={{width:'20%',textAlign:'center',borderRightWidth:1}}>{value.cantidad}</Text>
            <Text style={{width:'20%',textAlign:'center',borderRightWidth:1}}>s/ {value.total}</Text>
        </TouchableOpacity>
        
    ))
  
    return (
        <View style={styles.container}>
            <View style={{height:"30%",justifyContent:'center',alignItems:'center'}}>
                <TouchableOpacity style={{backgroundColor:'cyan',width:'80%',alignItems:'center',borderRadius:12}}>
                    <Text style={{fontSize:22}}>Guardar</Text>
                </TouchableOpacity>
            </View>
            <View style={{flexDirection:'row',justifyContent:'center',alignItems:'center' }}>
                <Text style={{width:'30%',borderWidth:1,textAlign:'center'}}>Producto</Text>
                <Text style={{width:'30%',borderWidth:1,textAlign:'center'}}>P/U</Text>
                <Text style={{width:'20%',borderWidth:1,textAlign:'center'}}>CAN</Text>
                <Text style={{width:'20%',borderWidth:1,textAlign:'center'}}>T s/</Text>
            </View>
            {/* <EventListProduc data={productos}/> */}
            {renderItem}
            <View style={{justifyContent:'flex-end',width:'100%',alignContent:'flex-end',alignItems:'flex-end'}}>
                <Text style={{marginRight:20}}>Total s/ {sumar()}</Text>
            </View>
        </View>
    );
}
const styles = StyleSheet.create({
    container : {
        fleax:1,
        backgroundColor:'fff1',
    },
    element :{
        width:"100%",
            
    }
});
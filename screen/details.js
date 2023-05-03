import  {useNavigation, useRoute} from '@react-navigation/native'
import { useContext, useLayoutEffect, useState } from 'react';
import { TextInput } from 'react-native';
import { View,StyleSheet ,Text,TouchableOpacity} from "react-native";
import { Contex } from './context';


export const Detail =() => {

    const globalContex = useContext(Contex);
    const {productos,setProductos} = globalContex;
    const route = useRoute();
    const navigation  = useNavigation();
    const {data} = route.params;
    const [cantidad,setCantidad] = useState('1');
    const [precio,setPrecio] = useState('0.00')
   
    useLayoutEffect(()=>{
        navigation.setOptions({
            headerTitle:'Producto Seleccionado',
            headerTitleAlign:'center'
            
            
        })
    },[])
    const desc =(cantidad,precio,descuento)=>{
        try{
            return (cantidad*precio*(1-descuento/100)).toFixed(2);
        }catch{
            return '0.00';
        }
    }
    const addDates =()=>{
        const datos = {id:data[0],producto:data[1],descripcion:data[2],precio:precio,cantidad:cantidad,total:desc(cantidad,precio,data[5])}
        console.log(datos)
        setProductos([...productos,datos])
        navigation.navigate('Carrito')
    }
    return(
        <View style={styles.home}>
            <View  style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt} >Producto: </Text>
                <Text style={[styles.txt,{borderBottomWidth:1}]} >{data[1]}</Text>
            </View>
            <View  style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Descripcion: </Text>
                <Text style={[styles.txt,{borderBottomWidth:1}]}>{data[2]}</Text>
            </View>
            <View style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Precio</Text>
                <TextInput style={styles.txtinput} value={precio} onChangeText={setPrecio} selectTextOnFocus={true} keyboardType='numeric'/>
            </View>
            <View style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Cantidad</Text>
                <TextInput style={styles.txtinput}  value={cantidad} onChangeText={setCantidad} selectTextOnFocus={true} keyboardType='numeric'/>
            </View>
            <View style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Descuento</Text>
                <Text style={[styles.txt,{borderBottomWidth:1}]} >{data[5]}%</Text>
            </View>
            <View style={{flexDirection:'row' ,justifyContent:'space-between'}} >
                <Text style={styles.txt}>Total  </Text>
                <Text  style={styles.txt}>s/ {desc(cantidad,precio,data[5])}</Text>
            </View>
            <TouchableOpacity style={styles.btn} onPress={()=>addDates()}>
                <Text style={{fontSize:20}}>Agregrar</Text>
            </TouchableOpacity>
        </View>
    )
    
}
const styles = StyleSheet.create({
    home:{
        padding:20,
        fontSize:30,

    },
    txt:{
        fontSize:22,
        color:'#000',
        width:'50%',
        
        justifyContent:'space-between'
    },
    txtinput:{
        fontSize:22,
        borderWidth:1,
        paddingTop:10,
        marginTop:10,
        width:"50%",
        textAlign:'center',
        marginLeft:12,
        textShadowColor:'#000'
        
    },
    btn:{
        width:'100%',
        backgroundColor:'#abcdef',
        height:30,
        justifyContent:'center',
        alignItems:'center',
        borderRadius:15,
    }
})
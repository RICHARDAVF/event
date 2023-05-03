import { DrawerItemList, DrawerItem, createDrawerNavigator } from '@react-navigation/drawer';
import { HomeStack, ListaStack, ProfileStack } from './stack';
import { Image, SafeAreaView, Linking, View } from 'react-native';
import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';
const Drawer = createDrawerNavigator();

export const MyDrawer = ({status }) => {
  const handleLogout =  () => {
    // Eliminar el token
      status(true)
      AsyncStorage.removeItem('token');
   
  };

  return (
    <Drawer.Navigator
      drawerContent={(props) => {
        return (
          <SafeAreaView style={{ flex: 1, paddingTop: 20 }}>
            <View style={{ justifyContent: 'center', alignItems: 'center' }}>
              <Image style={{ resizeMode: 'contain', width: 100 }} source={require('../assets/favicon.png')} />
            </View>
            <DrawerItemList {...props} />
            <DrawerItem
              label="Informacion"
              onPress={() => Linking.openURL('https://google.com')}
              icon={() => <Ionicons name="information-circle" size={22} />}
            />
          
            <DrawerItem
                label="Logout"
                onPress={() => handleLogout()}
                icon={() => <Ionicons name="log-out" size={22} />}
              />
            
          </SafeAreaView>
        );
      }}
      screenOptions={{
        headerShown: false,
      }}
    >
      <Drawer.Screen
        name="HomeStack"
        component={HomeStack}
        options={{ title: 'Inicio', drawerIcon: () => <MaterialCommunityIcons name="home" size={22} />}}
      />
      <Drawer.Screen name='ListaStack'
      component={ListaStack}
      options={{title:'Nota de Pedido',drawerIcon: () => <Ionicons name="cart" size={22} color="black" />}}
      />
      
      <Drawer.Screen
        name="ProfileStack0"
        component={'0'}
        options={{ title: 'Cotizacion', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
      <Drawer.Screen
        name="ProfileStack1"
        component={'1'}
        options={{ title: 'Estado de cotizacion', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
      <Drawer.Screen
        name="ProfileStack2"
        component={'2'}
        options={{ title: 'Estado de Pedidos', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
      <Drawer.Screen
        name="ProfileStack3"
        component={'3'}
        options={{ title: 'Aprobacion de Pedidos', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
      <Drawer.Screen
        name="ProfileStack4"
        component={'4'}
        options={{ title: 'Facturacion Electronica', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
      <Drawer.Screen
        name="ProfileStack5"
        component={'5'}
        options={{ title: 'Estado de Documentos', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
      <Drawer.Screen
        name="ProfileStack6"
        component={'6'}
        options={{ title: 'Cuentas ¨por cobrar', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
      <Drawer.Screen
        name="ProfileStack7"
        component={'7'}
        options={{ title: 'Registro de ventas', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
      <Drawer.Screen
        name="ProfileStack8"
        component={'8'}
        options={{ title: 'Ventas Tabuladas', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
    </Drawer.Navigator>
  );
};

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
        options={{ title: 'Home', drawerIcon: () => <MaterialCommunityIcons name="home" size={22} />}}
      />
      <Drawer.Screen name='ListaStack'
      component={ListaStack}
      options={{title:'Nota de Venta',drawerIcon: () => <Ionicons name="cart" size={22} color="black" />}}
      />
      
      <Drawer.Screen
        name="ProfileStack"
        component={ProfileStack}
        options={{ title: 'Profiles', drawerIcon: () => <MaterialCommunityIcons name="face-man" size={22} /> }}
      />
    </Drawer.Navigator>
  );
};

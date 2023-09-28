import { StatusBar } from 'expo-status-bar';
import { SafeAreaView, StyleSheet, Text, View } from 'react-native';
import { Video, ResizeMode } from 'expo-av';

export default function App() {
  return (
    <SafeAreaView >
      <Text>Words Here !!!!!!!</Text>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  video: {
    height: "100%",
    width: "100%"
  }
});

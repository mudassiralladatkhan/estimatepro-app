import sys
import traceback
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.logger import Logger

# Import screen classes from your modules
try:
    from screens.concrete import ConcreteScreen
    from screens.steel import SteelScreen
    from screens.brick import BrickScreen
    from screens.block import BlockScreen
    from screens.paint import PaintScreen
    from screens.excavation import ExcavationScreen
    from screens.filling import SlopeFillingScreen
    from screens.antitermite import AntiTermiteScreen
    from screens.plaster import PlasterScreen
    from screens.watertank import WaterTankScreen
    from screens.tile import TileScreen
    from screens.dashboard import DashboardScreen
    from screens.homescreen import HomeScreen
    from screens.auth import AuthScreen
    Logger.info("EstimatePro: All screens imported successfully")
except Exception as e:
    Logger.error(f"EstimatePro: Error importing screens: {e}")
    Logger.error(traceback.format_exc())

class EstimateProApp(App):
    def build(self):
        try:
            sm = ScreenManager(transition=FadeTransition())

            # Add all screens to the ScreenManager
            sm.add_widget(HomeScreen(name='home'))
            sm.add_widget(AuthScreen(name='auth'))
            sm.add_widget(DashboardScreen(name='dashboard'))
            sm.add_widget(ConcreteScreen(name='concrete'))
            sm.add_widget(SteelScreen(name='steel'))
            sm.add_widget(BrickScreen(name='bricks'))
            sm.add_widget(PlasterScreen(name='plaster'))
            sm.add_widget(PaintScreen(name='paint'))
            sm.add_widget(TileScreen(name='tiles'))
            sm.add_widget(SlopeFillingScreen(name='slopefilling'))
            sm.add_widget(ExcavationScreen(name='excavation'))
            sm.add_widget(AntiTermiteScreen(name='antitermite'))
            sm.add_widget(BlockScreen(name='blocks'))
            sm.add_widget(WaterTankScreen(name='watertank'))

            Logger.info("EstimatePro: App built successfully")
            return sm
        except Exception as e:
            Logger.error(f"EstimatePro: Error building app: {e}")
            Logger.error(traceback.format_exc())
            raise

if __name__ == '__main__':
    try:
        EstimateProApp().run()
    except Exception as e:
        Logger.error(f"EstimatePro: Fatal error: {e}")
        Logger.error(traceback.format_exc())
        sys.exit(1)

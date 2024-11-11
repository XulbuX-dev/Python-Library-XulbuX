from src.XulbuX import rgba, hexa, hsla

clr_rgba = (255, 0, 0, 0.5)
clr_hexa = '#FF00007F'
clr_hsla = (0, 100, 50, 0.5)

def test_rgba():
    clr_rgba = (255, 0, 0, 0.5)
    assert isinstance(rgba(*clr_rgba).to_hsla(), hsla)
    assert isinstance(rgba(*clr_rgba).to_hexa(), hexa)
    assert isinstance(rgba(*clr_rgba).has_alpha(), bool)
print(f'lighten(0.5): {rgba(*clr_rgba).lighten(0.5)}')
print(f'darken(0.5): {rgba(*clr_rgba).darken(0.5)}')
print(f'saturate(0.5): {rgba(*clr_rgba).saturate(0.5)}')
print(f'desaturate(0.5): {rgba(*clr_rgba).desaturate(0.5)}')
print(f'rotate(90): {rgba(*clr_rgba).rotate(90)}')
print(f'rotate(-90): {rgba(*clr_rgba).rotate(-90)}')
print(f'invert(): {rgba(*clr_rgba).invert()}')
print(f'grayscale(): {rgba(*clr_rgba).grayscale()}')
print(f'blend((0, 255, 0)): {rgba(*clr_rgba).blend((0, 255, 0))}')
print(f'is_dark(): {rgba(*clr_rgba).is_dark()}')
print(f'is_light(): {rgba(*clr_rgba).is_light()}')
print(f'is_grayscale(): {rgba(*clr_rgba).is_grayscale()}')
print(f'is_opaque(): {rgba(*clr_rgba).is_opaque()}')
print(f'with_alpha(0.5): {rgba(*clr_rgba).with_alpha(0.5)}')
print(f'complementary(): {rgba(*clr_rgba).complementary()}')

print(f'\n------ {hsla(*clr_hsla)} ------')
print(f'to_rgba(): {hsla(*clr_hsla).to_rgba()}')
print(f'to_hexa(): {hsla(*clr_hsla).to_hexa()}')
print(f'has_alpha(): {hsla(*clr_hsla).has_alpha()}')
print(f'lighten(0.5): {hsla(*clr_hsla).lighten(0.5)}')
print(f'darken(0.5): {hsla(*clr_hsla).darken(0.5)}')
print(f'saturate(0.5): {hsla(*clr_hsla).saturate(0.5)}')
print(f'desaturate(0.5): {hsla(*clr_hsla).desaturate(0.5)}')
print(f'rotate(90): {hsla(*clr_hsla).rotate(90)}')
print(f'rotate(-90): {hsla(*clr_hsla).rotate(-90)}')
print(f'invert(): {hsla(*clr_hsla).invert()}')
print(f'grayscale(): {hsla(*clr_hsla).grayscale()}')
print(f'blend((120, 100, 50)): {hsla(*clr_hsla).blend((120, 100, 50))}')
print(f'is_dark(): {hsla(*clr_hsla).is_dark()}')
print(f'is_light(): {hsla(*clr_hsla).is_light()}')
print(f'is_grayscale(): {hsla(*clr_hsla).is_grayscale()}')
print(f'is_opaque(): {hsla(*clr_hsla).is_opaque()}')
print(f'with_alpha(0.5): {hsla(*clr_hsla).with_alpha(0.5)}')
print(f'complementary(): {hsla(*clr_hsla).complementary()}')

print(f'\n------ {hexa(clr_hexa)} ------')
print(f'to_rgba(): {hexa(clr_hexa).to_rgba()}')
print(f'to_hsla(): {hexa(clr_hexa).to_hsla()}')
print(f'has_alpha(): {hexa(clr_hexa).has_alpha()}')
print(f'lighten(0.5): {hexa(clr_hexa).lighten(0.5)}')
print(f'darken(0.5): {hexa(clr_hexa).darken(0.5)}')
print(f'saturate(0.5): {hexa(clr_hexa).saturate(0.5)}')
print(f'desaturate(0.5): {hexa(clr_hexa).desaturate(0.5)}')
print(f'rotate(90): {hexa(clr_hexa).rotate(90)}')
print(f'rotate(-90): {hexa(clr_hexa).rotate(-90)}')
print(f'invert(): {hexa(clr_hexa).invert()}')
print(f'grayscale(): {hexa(clr_hexa).grayscale()}')
print(f'blend("#0F0"): {hexa(clr_hexa).blend("#0F0")}')
print(f'is_dark(): {hexa(clr_hexa).is_dark()}')
print(f'is_light(): {hexa(clr_hexa).is_light()}')
print(f'is_grayscale(): {hexa(clr_hexa).is_grayscale()}')
print(f'is_opaque(): {hexa(clr_hexa).is_opaque()}')
print(f'with_alpha(0.5): {hexa(clr_hexa).with_alpha(0.5)}')
print(f'complementary(): {hexa(clr_hexa).complementary()}')

print()  # SPACE AFTER LAST LINE

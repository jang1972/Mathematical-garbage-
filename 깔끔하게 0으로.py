import traceback
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, jv, zeta
import fuckit

# ★ NumPy 연산 중 0으로 나누는 경고가 발생하면 에러(Exception)를 던지도록 설정
np.seterr(divide='raise') 

@fuckit
def calculate_latex_expression(n_max: int = 1000, k_max: int = 1000) -> float:
    try:
        # (기존 계산 로직 동일)
        integral_ln_sin, _ = quad(np.log, 0, np.pi)
        numerator_sum = sum(((-1)**n * zeta(2*n) / gamma(n + 1)) for n in range(1, n_max + 1))
        numerator = numerator_sum * integral_ln_sin

        integral_gaussian_sin, _ = quad(lambda x: np.exp(-x**2) * np.sin(x), -np.inf, np.inf)
        product_cosh = np.prod([np.cosh(1/m) for m in range(1, k_max + 1)])
        sum_bessel = sum(np.sqrt(j**2 + 1) / zeta(0) * jv(0, float(j)) for j in range(k_max + 1))
        denominator = (product_cosh - sum_bessel) * integral_gaussian_sin

        return numerator / denominator
    
    except Exception:
        traceback.print_exc()
        raise


# 실행 예시
if __name__ == "__main__":
    result = calculate_latex_expression()
    print(f"계산된 최종 값: {result}")

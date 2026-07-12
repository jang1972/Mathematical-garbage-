import traceback
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, jv, zeta, jn_zeros
import fuckit

np.seterr(divide='raise') 

@fuckit
def calculate_latex_expression(n_max: int = 1000, k_max: int = 1000) -> float:
    try:
        integral_ln_sin, _ = quad(lambda x: np.log(np.sin(x)), 0, np.pi)
        numerator_sum = sum(((-1)**n * zeta(2*n) / gamma(n + 1)) for n in range(1, n_max + 1))
        numerator = numerator_sum * integral_ln_sin

        integral_gaussian_sin, _ = quad(lambda x: np.exp(-x**2) * np.sin(x), -np.inf, np.inf)
        product_cosh = np.prod([np.cosh(1/m) for m in range(1, k_max + 1)])
        
        # alpha_j (J_0의 영점들) 생성: j=1부터 k까지의 영점 (alpha_0은 0으로 설정)
        zeros = jn_zeros(0, k_max)
        alpha = np.insert(zeros, 0, 0.0)
        
        sum_bessel = sum(jv(0, alpha[j]) / np.sqrt(j**2 + 1) for j in range(k_max + 1))
        denominator = (product_cosh - sum_bessel) * integral_gaussian_sin

        return numerator / denominator
    
    except Exception:
        traceback.print_exc()
        raise


if __name__ == "__main__":
    result = calculate_latex_expression()
    print(f"계산된 최종 값: {result}")
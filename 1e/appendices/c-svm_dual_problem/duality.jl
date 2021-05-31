### A Pluto.jl notebook ###
# v0.14.7

using Markdown
using InteractiveUtils

# This Pluto notebook uses @bind for interactivity. When running this notebook outside of Pluto, the following 'mock version' of @bind gives bound variables a default value (instead of an error).
macro bind(def, element)
    quote
        local el = $(esc(element))
        global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : missing
        el
    end
end

# ╔═╡ e1899b13-b53d-40d4-8278-782d733026dc
using PlutoUI  # Slider, etc. is in PlutoUI

# ╔═╡ 7ccac76a-c21d-11eb-192b-d3a363901999
md"""
## First Example: Lagrange Multipliers Method
Find extremum of the following function

$$f(x,y) = x^2 + 2y$$

constrained to ``3x + 2y + 1 = 0\,.``

Actually, in the book, it was written **"find minimum"**.$(HTML("<br>"))

**(?)** How do we know right from the start that it concerns a minimum and not a maximum?$(HTML("<br>"))
**(R)** A few viewpoints
- Any straight line, as long as not vertical, admits as equation $y = ax + b$. When substituting into $f$, we have $f(x,y) = x^2 + 2(ax + b)$. No matter how negative $a$ and $b$ get, we see that $x^2 + 2(ax + b)$ will always eventually be dominated by the $x^2$ term. In other words, as $x \to \infty$, we will always have $f(x,y) \to \infty\,.$ So, the extremum must be a minimum.
  - This explains, but feels lengthy.
- Here, in the first part of this Pluto notebook, I would like to do a visualization of this.
"""

# ╔═╡ 42c5a4b3-c8b9-4792-aeed-6d49b84f844e
oft = Base.Filesystem.homedir() * "/.config/julia/projects/oft"

# ╔═╡ 9670a6b0-6376-47bb-946b-4cb5c9accbb7
begin
  using Pkg
  Pkg.activate(oft)
end

# ╔═╡ 3de8d308-1c92-4485-840e-750caefef3b5
@bind x Slider(-100:0.5:100, show_value=true, default=0)

# ╔═╡ ae61b0b5-c8da-40b9-b2aa-f7e11ae96592
f(x, y) = x^2 + 2y

# ╔═╡ c2f23acb-1a24-4812-bca0-f1861c67d690
y = (-3x - 1) / 2

# ╔═╡ a0ca56a6-1a3f-4798-881f-badc9ecd9748
f(x, y)

# ╔═╡ Cell order:
# ╟─7ccac76a-c21d-11eb-192b-d3a363901999
# ╠═42c5a4b3-c8b9-4792-aeed-6d49b84f844e
# ╠═9670a6b0-6376-47bb-946b-4cb5c9accbb7
# ╠═e1899b13-b53d-40d4-8278-782d733026dc
# ╠═3de8d308-1c92-4485-840e-750caefef3b5
# ╠═ae61b0b5-c8da-40b9-b2aa-f7e11ae96592
# ╠═c2f23acb-1a24-4812-bca0-f1861c67d690
# ╠═a0ca56a6-1a3f-4798-881f-badc9ecd9748

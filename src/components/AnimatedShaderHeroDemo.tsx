import Hero from "~/components/ui/animated-shader-hero";

// Demo component showing how to use the Hero
export default function AnimatedShaderHeroDemo() {
	const handlePrimaryClick = () => {
		console.log("Get Started clicked!");
		// Add your logic here
	};

	const handleSecondaryClick = () => {
		console.log("Explore Features clicked!");
		// Add your logic here
	};

	return (
		<div className="w-full">
			<Hero
				trustBadge={{
					text: "Trusted by forward-thinking teams.",
					icons: ["✨"],
				}}
				headline={{
					line1: "Launch Your",
					line2: "Workflow Into Orbit",
				}}
				subtitle="Supercharge productivity with AI-powered automation and integrations built for the next generation of teams — fast, seamless, and limitless."
				buttons={{
					primary: {
						text: "Get Started for Free",
						onClick: handlePrimaryClick,
					},
					secondary: {
						text: "Explore Features",
						onClick: handleSecondaryClick,
					},
				}}
			/>
		</div>
	);
}
